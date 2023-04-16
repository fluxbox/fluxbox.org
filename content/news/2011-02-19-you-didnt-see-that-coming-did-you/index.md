---
title: |
  2011-02-19 19:50:02 - You didn't see that coming, did you?
author: "The Fluxbox Team"
date: "2011-02-19 19:50:02"
---

# You didn't see that coming, did you?

Fluxbox 1.3 has arrived! A long long long time is over, and we finally
decided to make a release.

* Added support for bidirectional text, #2801836.
* Allow to override 'Focus New Windows' via .fluxbox/apps
* New actions:
  * ActivateTab
  * ArrangeWindowsVertical
* New 'MoveN' and 'ClickN' action support for keys file
* New focus model 'StrictMouseFocus'. This will affect focus when
  closing, moving, lowering windows, changing desktops, etc, whereas the
  'MouseFocus' model will only change focus when you move the mouse.
* New "background: unset" property for use in overlays.
* Allowing relative paths for background images in style files.
* Allowing matching screen number in ClientPattern.
* Removed rootcommand from init, as fbsetbg is run automatically nowadays.
* Removed line style resources from init file.

In any case, we hope to get more into the 'flux' way of doing things, aka
release early and often. So, have fun with this release.

Personal note from Mathias: This one is dedicated to the first official
'fluxbaby' on the planet: my daughter Karo, born on 6th of November 2010.
Which is, btw, the birthday of Henrik as well :)



