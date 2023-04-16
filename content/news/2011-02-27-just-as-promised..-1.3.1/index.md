---
title: |
  2011-02-27 19:00:54 - Just as promised... 1.3.1!
author: "Mathias"
date: "2011-02-27 19:00:54"
---

# Just as promised... 1.3.1!

Getting the 1.3.0 out of the door brought up some hidden bugs, we tried
hard to catch most of them in the last week. Since that went very well,
we have a new release for you:

Critical Bugfixes:

* Fix for not hiding submenus if menuDelay is set.
* Fix crash when moving transient windows (Dialogs) between Workspaces,
  #3088856.
* Fix crash when SystemTray was rotated 90/270 degree, #3188223.
* Fix potential crash when gettting an UnmapEvent before a FocusEvent.
* Fix potential crash on accessing NULL-pointer.

Other Bugfixes:

* Fix wrong width calculation of Systemtray, #3150939.
* Fix initial placement of WindowMenu, #2731524.
* Fix incorrectly shown alpha values in Menus, #3187373.
* Fix render 'sunken' Textures correctly.

Personal note from Mathias: This is the first time 'fluxgen' was not
able to get this release out of the door himself. He has injured himself
by trying something a real hacker should never be allowed: Leave the
keyboard. So, best whishes from here towards Henrik!



