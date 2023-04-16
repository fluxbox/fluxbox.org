---
title: |
  2002-05-24 22:30:00 - Fluxbox 0.1.9 Released
author: "Henrik"
date: "2002-05-24 22:30:00"
---

# Fluxbox 0.1.9 Released

Get it <a
href="http://prdownloads.sourceforge.net/fluxbox/fluxbox-0.1.9.tar.gz">here</a><br>
<b>News for 0.1.9:</b>
<ul>
<li>Improved fluxbox-generate_menu script.
 Which now installs itself so you can <br>
 regenerate the menu any time,and with gnome and kde menus<br>
 run: fluxbox-generate_menu -h<br>
 for more information.<br>

<li>Default 24 hour clock format<br>
<li>Code cleaning<br>
<li>Compiles with no errors on Mac OS X
<li>Now compiles with Intel Compiler 6.0 and GCC 3.1
<li>New keybindings:
	<blockquote>
    	<li><b>FirstTab</b><br>
	    Go to first tab
		<br><br>

		<li><b>LastTab</b><br>
		Go to last tab
		<br><br>

		<li><b>MoveTabPrev</b><br>
		Move current tab left
		<br><br>

		<li><b>MoveTabNext</b><br>
		Move current tab right
	</blockquote>
<li>"Allow Desktop MouseWheel Switching" runtime option
<li>Configurable geometry show
    configure in init with: session.screen0.showwindowposition<br>
<li>Now saves resources when you change them in the menu and not when you
    exit Fluxbox. So you can edit the init file and the reconfigure/restart <br>
    Fluxbox to activate changes.<br>
</ul>
<b>Bugfixes: </b><br>
<ul>
	<li>bug [ 552723 ] removing decorations while shaded.
	<li>shade bug while vertical rotated tabs and tabs off
 	<li>bug [ 515483 ] "XMMS Problem"
	<li>Fixed transient bug which cause Fluxbox to crach ( the "acroread" bug )
</ul>
Enjoy.
<br><br>

<i>U: 16:45 by aleczapka</i>: If you want to enable NLS support use <a href="/download/patches/fluxbox-0.1.9-bugfix1.patch">this patch</a>.





