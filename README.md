# AwakeGuardian

[English](https://github.com/kamil-cy/awake-guardian/blob/main/README.md), [Polski](https://github.com/kamil-cy/awake-guardian/blob/main/README.pl.md)

## About
**AwakeGuardian** is a program that helps you keep awake and not to fall asleep in front of a computer. 
The program frequently alerts you when detects your inactivity by reminding or later by nagging you using sound.
Moreover to save your money your computer can be suspended or powered off.
It was design to use as low memory as it is possible, so a few trade-offs has been taken.

## Installation
```pip install awake-guardian```

**_Warning_**: If you are using Python 3.10 on Windows then `Microsoft Visual C++ 14.0 or greater` is required. You can get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
So if you want **Awake Guardian** working just after pip installation on Windows, please use Python 3.9.

## Requirements
**AwakeGuardian** requires Python 3.6 or above.
It relies on different packages according to the system that you use.
All requirements should be installed automatically.

## Platforms
The program is working on Linux and Windows, and tries to work the same on any of each.
Due to some technical differences between systems there are only few different approaches to some aspects of how the program works.

**AwakeGuardian** it's just a script without a file extension that can be run simply as a command: `AwakeGuardian`

### Linux
On Linux this command can be typed wherever it's acceptable to pass a command to run.

### Windows
On Windows you can run the program by typing the command using *cmd*, *PowerShell* or *Run dialog box* (keyboard shortcut *Logo+R*), however environment variable *PATH* has to be configured properly, which can be done when installing Python if *Add Python to PATH* is checked.

## Using

### System tray icon
**AwakeGuardian** is working in the background and hasn't got any main window, only an icon is visible in the system notification area or system tray. 

![systray](https://github.com/kamil-cy/awake-guardian/raw/main/docs/systray_red_arrow.png)

**AwakeGuardian** is displaying icons according to the current state of the program.

- ![clock](https://github.com/kamil-cy/awake-guardian/raw/main/awake_guardian/images/clock.png) waiting for specified time window in which the program can work

- ![eyes](https://github.com/kamil-cy/awake-guardian/raw/main/awake_guardian/images/eyes.png) activity is being detected, neither of timers are exceeded, click this icon to pause

- ![beep](https://github.com/kamil-cy/awake-guardian/raw/main/awake_guardian/images/beep.png) short inactivity detected, remind timer is exceeded, remind sound is played in the loop until any detected activity

- ![shout](https://github.com/kamil-cy/awake-guardian/raw/main/awake_guardian/images/shout.png) long inactivity detected, nag timer is exceeded, nag sound is played in the loop, and by default the system volume is getting louder until any detected activity, later volume level is restored to the previous state 

- ![inactive](https://github.com/kamil-cy/awake-guardian/raw/main/awake_guardian/images/inactive.png) the program is paused, click this icon to resume

### Pause/Resume
When you left click on the **AwakeGuardian** icon, you'll see the pause dialog.

![pause_dialog_en](https://github.com/kamil-cy/awake-guardian/raw/main/docs/pause_dialog_en.png)

After closing this dialog, the systray menu will change to e.g.:

![systray_menu_en](https://github.com/kamil-cy/awake-guardian/raw/main/docs/systray_menu_en.png)

### Settings
**AwakeGuardian** can be configured in the settings dialog. 
You can adjust reminder or nag timers, toggle volume incrementing when reminding or nagging and toggle running the program on system startup.
Also you can adjust the time window in which the program can work.

Using power management section you can determine the time after which a specified action can occur for energy saving.
Depending on the capabilities of the operating system, the available options are:
- `Poweroff` turns off the computer after a preset time of inactivity.
- `Suspend` puts the computer into a low-power state with the ability to quickly resume operation.
- `Hibernate` causes the computer to go into deep sleep (hibernation), which minimizes energy consumption, memory dump is usually saved on the hard disk, so resuming work is slower than in the suspend mode, however this mode is not always supported.
- `Hybrid sleep` is a combination of suspend and hibernation where your programs and opened files reside in the computer memory as if in the suspend mode, and then the memory state is dumped to the hard drive as if in the hibernation mode, so you can quickly resume work and in the case of a power loss the system will resume as if in the hibernation mode.
- `Suspend then hibernate` puts the computer into the suspend mode, and when the time limit or the remaining battery power is exceeded, the computer will hibernate, which unlike the hybrid sleep mode, will not cause the battery to be completely depleted as if in the sleep mode.

![settings_dialog_en](https://github.com/kamil-cy/awake-guardian/raw/main/docs/settings_dialog_en.png)

#### Settings profiles

```
Profile                                  | Remind     | Nag        | Power management
-----------------------------------------+------------+------------+------------------
Slow falling asleep                      | yes, 10:00 | yes, 15:00 | no
Quick falling asleep                     | yes, 05:00 | yes, 10:00 | no
Power saving                             | no         | no         | yes, 10:00, Sleep
Extreme power saving                     | no         | no         | yes, 05:00, Sleep
Power saving with remind                 | yes, 09:00 | no         | yes, 10:00, Sleep
Extreme power saving with remind         | yes, 04:00 | no         | yes, 05:00, Sleep
Power saving with remind and nag         | yes, 08:00 | yes, 09:00 | yes, 10:00, Sleep
Extreme power saving with remind and nag | yes, 03:00 | yes, 04:00 | yes, 05:00, Sleep
```
