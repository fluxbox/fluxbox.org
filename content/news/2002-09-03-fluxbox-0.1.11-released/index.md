---
title: |
  2002-09-03 15:50:00 - Fluxbox 0.1.11 Released
author: "Henrik"
date: "2002-09-03 15:50:00"
---

# Fluxbox 0.1.11 Released

Get it  <a
href="http://prdownloads.sourceforge.net/fluxbox/fluxbox-0.1.11.tar.gz">here</a><br>
<b>News in 0.1.11:</b>
<ul>
  <li>Autogrouping:<br>
      This will read groups from a file and auto group programs when they start.<br>
  <li>Autogrouping-from-tab:<br>
      This will allow you to popup the root menu, if you right click on the tab,
	  and select an application and it'll start grouped to the tab.
      (note: this might interfere with the normal autogrouping in a bad way) <br>
  <li>Two new themes: BlueNight and LemonSpace<br>
  <li>Carry window across workspace with outlined mode.<br>
  <li>Slit now has a theme option:<br>
    <blockquote>
      slit: [texture option]<br>
      slit.color: [color value]<br>
      slit.colorTo: [color value]<br>
      It will fall back to the toolbar theme if it doesn't find it.<br>
	</blockquote>
   <li>ja_JP and fr_FR in fluxbox-generate_menu<br>
   <li>New util: fbrun<br>
      Which allows you to type a command and run it.<br>
   <li>The window menu now pop up in iconbar when you right click on the icon.<br>
</ul>
<b>Bug fixes:</b><br>
<ul>
   <li>Fixed bug [ 582574 ] borderless windows cant be horiz resized.
   <li>Fixed bug [ 600811 ] undefined keys messes up
   <li>Fixed bug [ 598490 ] misplaced parentrelative gives redrw prb
   <li>Fixed bug [ 586830 ] the clock now updates once per second.
   <li>Fixed bug [ 574717 ] restarting fluxbox should keep iconic.
   <li>Fixed "send to..." bug
   <li>Fixed slitlist bug
   <li>Fixed workspace name and the reassociation bug
</ul>
(The transient bug might be fixed but needs more testing, so if you filled a bugreport about transient window, please verify this)<br>
Enjoy.



