---
title: |
  2015-02-08 13:57:55 - Fluxbox 1.3.7 - Bam! Zero Bugs!!11!
author: "The Fluxbox team"
date: "2015-02-08 13:57:55"
---

# Fluxbox 1.3.7 - Bam! Zero Bugs!!11!


To release 1.3.6 ~ a month ago was a great success: A lot of you, our
users, who rarely run bleeding edge fluxbox.git, were confronted with
what was hidden in the git repository for almost 2 years. Due to the
lack of testing power there was no other way to get "massive"
feedback.  1.3.6 generated the feedback we needed to make 1.3.7. There
will be bugs, obviously, but we think 1.3.7 is in pretty good shape.
Without further ado:

Critical Bugfixes:

* Segfault on startup (mostly *BSD)
* Segfault on shutdown
* Segfault on clicking the Remember menu
* Menu crops on TypeAhead

Minor Bugfixes:

* \_NET\_REQUEST\_FRAME\_EXTENTS
* Working autorepeat keys
* Working vertical rotated Tabs and Toolbar
* Proper size of titlebar buttons on restart / detaching tabs
* Missing windowmenu works again
* Several glitches in the menu
* Correct handling of 'maximized' statement in the apps file

Features:

* The improved TypeAhead sytem is not limited to matches on beginning
  of menu items anymore, the behavior is configurable:
  * Nowhere - disables TypeAhead support
  * ItemStart - matches typed text only at the start of a menu item
  * Somewhere - matches typed text somewhere in a menu item
    (Currently this is a configfile-only option)

* Minor tweaks to the i18n system
* Updated turkish translations

End User unrelated:

* Code refactoring and cleanup, assisted by Coverity and
  clang static code analysis

Get it at the usual places, <a href="/download/">downloading the source</a>
is one option.



