---
title: |
  2012-12-30 21:01:41 - The world did not end - let's release 1.3.3
author: "The Fluxbox team"
date: "2012-12-30 21:01:41"
---

# The world did not end - let's release 1.3.3

So, the world is still rotating around the sun and before our calendar hits
2013 we decided to release a new stable version of fluxbox. This is mostly
a bugfix release.

General:

* Added 'NearestCorner', 'NearestEdge' and 'NearestCornerOrEdge' resize methods
* Added percentage values for commands such as ResizeWindow
* Added style ressources 'menu.hilite.font', 'menu.hilite.justify'
* Added 'OnTab' modifier for keys file
* Added _MOTIF\_WM\_INFO atom to advertise motif capabilities
* Added 'fullscreen', 'maximizedhorizontal', 'maximizedvertical' tests to client patterns
* Added option to revert focus to previous window only on current head in a multi-monitor setup
* Rewrite of FbTk::TextureRenderer (simpler code)
* Improved building on Microsoft Windows

Critical Bugfixes:

* Use of monotonic increasing clock for timer, not affected by leap seconds etc.

Other Bugfixes:

* Fixed placement off transient windows in a multi-monitor setup with 'holes'
* Fixed usage of '~' as part of style filenames
* Replaced (deprecated) XKeycodeToKeysym() with XkbKeycodeToKeysym()
* Improved vertical alignment of text in decorations
* Fixed compiler and code style issues
* Updated italian translations

Happy fluxboxing, great health, luck and everything else for 2013!



