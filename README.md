# Pipe Dream plugin for Sublime Text
## Pipes selected text through shell commands

#### [Sublime Text](http://www.sublimetext.com/)

## About
This is a Sublime Text plugin, allowing you to pipe selected text (multiple regions ok) or the buffer contents through arbitrary shell commands.

## Installation

Package Control -> Install Package -> Pipe Dream

## Usage

Either select a region (or regions) to operate on, or the plugin will use all the text in the window.

Goto: Tools -> Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`) and type any of the commands...

### Windows and Linux

***This plugin has not been tested on these platforms, but I expect it to work, I would appreciate if someone could let me know if it does, or if there are any issues***

## Commands

These commands are built in, and just to start you off. The idea is that you can easily define your own Pipe Dreams by editing the keymap files, or the commands file.

The keyboard shortcuts set by default, but can be edited easily in the relevant OS's keymap file.

- **Pipe Dream: Beautify JavaScript (uglifyjs)**
  - keys:`ctrl+alt+a b`
  - type: `text_replace`
  - cmds: `uglifyjs -b --comments all`
- **Pipe Dream: Minify JavaScript (uglifyjs)**
  - keys:`ctrl+alt+a u`
  - type: `text_replace`
  - cmds: `uglifyjs`
- **Pipe Dream: Execute JavaScript**
  - keys:`ctrl+alt+a x j`
  - type: `console_log`
  - cmds: `node`

## Customize

The `Sublime-Pipe-Dream.sublime-commands` file has some pre-defined commands, but you are strongly encouraged to make your own, and share them by [adding an issue](http://github.com/billymoon/Sublime-Pipe-Dream/issues) with your dreams.

## Oh no! command not found...

If you get an error `sh: node: command not found` or similar, maybe you don't have `node` (or similar) in the right path. Try setting the absolute path to node in `User/Sublime-Pipe-Dream.sublime-settings`.

This means from:
`"PATH": "/usr/sbin:/sbin:/usr/local/bin:"`

change to:
`"PATH": "/usr/sbin:/sbin:/usr/local/bin:/path/to/node/folder:"`

**Have fun!**

## Oh yeah!

Big thanks to Victor Porof for the original plugin I adapted: https://github.com/victorporof/Sublime-HTMLPrettify