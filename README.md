# Pipe Dream plugin for Sublime Text 2
## Pipes selected text through shell commands

#### [Sublime Text 2](http://www.sublimetext.com/2)

## About
This is a Sublime Text 2 plugin, allowing you to pipe selected text (multiple regions ok) or the buffer contents through shell commands.

## Installation
Each OS has a different `Packages` folder required by Sublime Text. Open it via Preferences -> Browse Packages, and copy this repository contents to the `Sublime-Pipe-Dream` folder there.

The shorter way of doing this is:

### Linux
`git clone git://github.com/billymoon/Sublime-Pipe-Dream.git ~/.config/sublime-text-2/Packages/Sublime-Pipe-Dream`

### Mac
`git clone git://github.com/billymoon/Sublime-Pipe-Dream.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Sublime-Pipe-Dream`

### Windows
`git clone git://github.com/billymoon/Sublime-Pipe-Dream.git %APPDATA%/Sublime\ Text\ 2/Packages/Sublime-Pipe-Dream`

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
- **Pipe Dream: Coffee Script To JavaSctipt (coffee)**
  - keys:`ctrl+alt+a j`
  - type: `text_replace`
  - cmds: `coffee -p -s -b`
- **Pipe Dream: JavaScript to Coffee Script (js2coffee)**
  - keys:`ctrl+alt+a c`
  - type: `text_replace`
  - cmds: `js2coffee`
- **Pipe Dream: Execute JavaScript**
  - keys:`ctrl+alt+a x j`
  - type: `console_log`
  - cmds: `node`
- **Pipe Dream: Execute Coffee Script**
  - keys:`ctrl+alt+a x c`
  - type: `console_log`
  - cmds: `coffee -s`
- **Pipe Dream: Markdown to HTML**
  - keys:`ctrl+alt+a m h`
  - type: `text_replace`
  - cmds: `marked`
- **Pipe Dream: HTML to Markdown**
  - keys:`ctrl+alt+a h m`
  - type: `text_replace`
  - cmds: `html2md`
- **Pipe Dream: Tidy HTML**
  - keys:`ctrl+alt+a t h`
  - type: `text_replace`
  - cmds: `tidy -i --tidy-mark no --show-body-only yes --wrap 0`
- **Pipe Dream: Execute MySQL**
  - keys:`ctrl+alt+a x m`
  - type: `console_log`
  - cmds: `mysql -u$u -p$p", "exports": "yes`
- **Pipe Dream: Encrypt (AES 256)**
  - keys:`ctrl+alt+a e`
  - type: `console_log`
  - cmds: `openssl aes-256-cbc -e -k $pw | openssl enc -base64", "exports": "ye`
- **Pipe Dream: Decrypt (AES 256)**
  - keys:`ctrl+alt+a d`
  - type: `console_log`
  - cmds: `openssl enc -base64 -d | openssl aes-256-cbc -d -k $pw", "exports": "ye`
- **Pipe Dream: Bash Shell**
  - keys:`ctrl+alt+a s`
  - type: `console_log`
  - cmds: `bash`
- **And my personal favourite... (OSX only, as it requires: textutil, pbcopy and marked)**
- **Pipe Dream: Render Markdown to Clipboard**
  - keys:`ctrl+alt+a m c`
  - type: `console_log`
  - cmds: `marked | textutil -stdin -format html -convert rtf -stdout | pbcopy -prefer rtf && echo rtf content is on the clipboard`

## Customize

The `Sublime-Pipe-Dream.py` file has some pre-defined commands, but you are strongly encouraged to make your own, and share them by [adding an issue](http://github.com/billymoon/Sublime-Pipe-Dream/issues) with your dreams.

## Oh no! command not found...

If you get an error `sh: node: command not found` or similar, maybe you don't have `node` (or similar) in the right path. Try setting the absolute path to node in `Sublime-Pipe-Dream.py`.

This means from:
`my_env["PATH"] = "/usr/sbin:/sbin:/usr/local/bin:" + my_env["PATH"]`

change to:
`my_env["PATH"] = "/usr/sbin:/sbin:/usr/local/bin:/path/to/node/folder" + my_env["PATH"]`

**Have fun!**

## Oh yeah!

Big thanks to Victor Porof for the original plugin I adapted: https://github.com/victorporof/Sublime-HTMLPrettify