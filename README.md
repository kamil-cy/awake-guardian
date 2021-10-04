# AwakeGuardian

[English](README.md), [Polski](README.pl.md)

## About
**AwakeGuardian** is a program that helps you keep awake and not to fall asleep in front of a computer. 
The program frequently alerts you when detects your inactivity by reminding or later by nagging you using sound.
It was design to use as low memory as it is possible, so a few trade-offs has been taken.

## Installation
```pip install awake-guardian```

## Requirements
**AwakeGuardian** requires Python 3.6 or above.
It relies on different packages according to the system that you use.
All requirements should be installed automatically.

## Platforms
**AwakeGuardian** is working on Linux and Windows, and tries to work the same on any system.
Due to some technical differences between systems there are only few different approaches to some aspects, like how to run the program.

### Linux
On Linux it's just a script without a file extension that can be run simply as a command.
Just type a command: `AwakeGuardian`

### Windows
On Windows, files (Python scripts) without an extension are very sophisticated to run, so to avoid all of this there is a simple batch script that runs the program without a console window.
Also just after installation on Windows the same batch file is put into your Desktop folder to make it easier to run it for the first time or make it run along with Windows start.
However you can run the program at any time without using the batch script by typing `AwakeGuardian.py` using *cmd* or *PowerShell*, but in that case you'll get also Python's console window that holds the running program, so closing this window closes the whole program.

## Using

### System tray icon
**AwakeGuardian** is working in the background and hasn't got any main window, only an icon is visible in the system notification area or system tray. 

![systray](docs/systray_red_arrow.png)

**AwakeGuardian** is displaying icons according to the current state of the program.

- ![clock](awake_guardian/images/clock.png) waiting for specified time window in which the program can work

- ![eyes](awake_guardian/images/eyes.png) activity is being detected, neither of timers are exceeded, click this icon to pause

- ![beep](awake_guardian/images/beep.png) short inactivity detected, remind timer is exceeded, remind sound is played in the loop until any detected activity

- ![shout](awake_guardian/images/shout.png) long inactivity detected, nag timer is exceeded, nag sound is played in the loop, and by default the system volume is getting louder until any detected activity, later volume level is restored to the previous state 

- ![inactive](awake_guardian/images/inactive.png) the program is paused, click this icon to resume

### Pause/Resume
When you left click on the **AwakeGuardian** icon, you'll see the pause dialog.

![pause_dialog_en](docs/pause_dialog_en.png)

After closing this dialog, the systray menu will change to e.g.:

![systray_menu_en](docs/systray_menu_en.png)

### Settings
**AwakeGuardian** can be configured in the settings dialog. 
You can adjust reminder or nag timers, toggle volume incrementing when nagging and toggle running the program on system startup.
Also you can adjust the time window in which the program can work.

![settings_dialog_en](docs/settings_dialog_en.png)