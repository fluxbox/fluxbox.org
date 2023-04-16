---
title: |
  2002-04-19 23:35:00 - Fluxbox 0.1.8 Released
author: "aleczapka"
date: "2002-04-19 23:35:00"
---

# Fluxbox 0.1.8 Released

News in Fluxbox 0.1.8:
<ul>
<li>Code clean up<br>
<li>NLS-fixes<br>
<li>Better window cycling with optional parameters.<br>
  NextWindow and PrevWindow now takes an integer parameter.<br>
  Parameter values:
	<blockquote>
     0 or unspecified = Default/current behavior - no skipping<br>
     1 = Skip: lower tabs<br>
     2 = Skip: stuck windows<br>
     3 = Skip: lower tabs/stuck windows<br>
     4 = Skip: shaded windows<br>
     5 = Skip: lower tabs/shaded windows<br>
     6 = Skip: stuck windows/shaded windows<br>
     7 = Skip: lower tabs/stuck windows/shaded windows
	</blockquote>
<li>Xinerama support ( configure option --enable-xinerama )
<li>Workspace warping, drag window between workspaces, does only work with opaque moving
<li>You can enable tabs in "Tabs off"-mode
<li>New key bindings:
	<blockquote>
		<li><b>ToggleDecor</b><br>
		Toggle the decor of a window
		<br><br>

		<li><b>ToggleTab</b><br>
	    Toggle the tab
		<br><br>

		<li><b>RootMenu</b><br>
      	Pop up the root menu
	</blockquote>
<li>Smarter Next/Prev focus,
  Makes new windows get inserted after the focused window in the cycling order instead of always at the end.
<li>Scrolling on root window changes workspace
</ul>
<br><br>

<b>Bug fixes in Fluxbox 0.1.8:</b><br>
<ul>
	<li>Window dragging + workspace changing ( bug [ 528101 ] )
	<li>Minor task bar issue, it will update icon bar-text now ( bug [ 533436 ] )
	<li>"decoration.handle" bug, which caused the window to have wrong height with no decorations
	<li>Slit-client window bug.
</ul>
Enjoy.




