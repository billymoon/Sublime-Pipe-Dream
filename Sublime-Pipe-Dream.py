import subprocess
import sublime
import sublime_plugin
import os
import json
import re

settings = sublime.load_settings(__name__ + '.sublime-settings')

my_env = os.environ.copy()

path = settings.get("PATH")
my_env["PATH"] = my_env["PATH"] + ":" + path
settings.set("PATH", path)

sublime.save_settings(__name__ + '.sublime-settings')

commands = file(__name__ + '.sublime-commands')
cmds = json.loads(commands.read())

cmd = { "caption": "Pipe Dream: Say", "command": "console_log" , "args": { "command": "say" } }
cmds.append(cmd)

def debug(message):
    if message is None:
        message = "NONE"
    # print type(message)
    print "DEBUG: "+json.dumps(message)


def set_exports(self, store, s, edit, command, root_command, remember_exports, console="no"):

    if len(store) > 0:
        if remember_exports == "yes":
            self.exports[root_command] = store
        command = "export " + store + "; " + command

    if console == "yes":
        self.execute(command, s)
    else:
        self.execute(edit, command)


def get_exports(self, command, s, exports, remember_exports):

    root_command = re.findall("^\w+", command)[0]

    if exports == "yes":
        try:
            command = "export " + self.exports[root_command] + "; " + command
            self.execute(command, s)
        except KeyError:
            self.view.window().show_input_panel("export:", '', lambda store: set_exports(self, store, s, self.edit, command, root_command, remember_exports, console="yes"), None, None)
    else:
        self.execute(command, s)


class ConsoleLogCommand(sublime_plugin.TextCommand):

    def __init__(self, view):

        if not hasattr(self, "exports"):
            self.exports = {}
        self.view = view

    def run(self, edit, command="", exports="", remember_exports="no"):

        root_command = re.findall("^\w+", command)[0]

        if exports == "yes":
            try:
                command = "export " + self.exports[root_command] + "; " + command
                self.execute(edit, command)
            except KeyError:
                self.view.window().show_input_panel("export:", '', lambda store: set_exports(self, store, "", edit, command, root_command, remember_exports), None, None)
        else:
            self.execute(edit, command)

    def clear_panel(self):

        edit = self.panel.begin_edit()
        self.panel.erase(edit, sublime.Region(0, self.panel.size()))
        self.panel.end_edit(edit)
        self.panel.set_read_only(True)

    def append_data(self, data):

        self.panel.set_read_only(False)
        edit = self.panel.begin_edit()
        self.panel.insert(edit, self.panel.size(), data)
        self.panel.end_edit(edit)
        self.panel.set_read_only(True)

    def create_panel(self):

        if not hasattr(self, 'panel'):
            self.panel = self.view.window().get_output_panel("panel")
        self.clear_panel()
        self.panel.set_read_only(False)

    def execute(self, edit, command):

        for region in self.view.sel():

            if region.empty():
                region = sublime.Region(0, self.view.size())

            if not region.empty():

                s = self.view.substr(region)

                echo = subprocess.Popen(['echo', s], stdout=subprocess.PIPE)
                ret = subprocess.Popen(command, shell=True, stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                self.create_panel()
                self.clear_panel()

                try:
                    output = ret.stdout.read().decode('utf-8')
                    self.append_data(output)
                except:
                    error = ret.stderr.read()
                    self.append_data(error)

                self.panel.set_read_only(True)

                self.view.window().run_command("show_panel", {"panel": "output.panel"})


class TextReplaceCommand(sublime_plugin.TextCommand):

    def __init__(self, view):

        if not hasattr(self, "exports"):
            self.exports = {}
        self.view = view

    def run(self, edit, command="", exports="", remember_exports="no"):

        self.edit = edit

        for region in self.view.sel():

            self.region = region

            if self.region.empty():
                self.region = sublime.Region(0, self.view.size())

            if not self.region.empty():

                s = self.view.substr(self.region)

                get_exports(self, command, s, exports, remember_exports)

    def execute(self, command, s):

        echo = subprocess.Popen(['echo', s], stdout=subprocess.PIPE)
        ret = subprocess.Popen(command, shell=True, stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ret.stdout.read().decode("utf-8")

        if len(output) > 0:
            self.view.replace(self.edit, self.region, output)
