---
title: |
  2002-04-30 02:30:00 - Development Continues: Patch of the Evening
author: "aleczapka"
date: "2002-04-30 02:30:00"
---

# Development Continues: Patch of the Evening

For quite a while, there is a lot going on at our <a href="http://www.geocrawler.com/lists/3/SourceForge/18605/0/">fluxbox-devel</a> mailing list.<br>
In a secret can tell ya, ppl are submitting patches like crazy... damn, how sweet :><br>
Some of them, got into v0.1.8 already, some are in current CVS, and some didn't make it yet.
You'd better take a look for yourself, cause you could loose a good chance to try some new,
really kewl features, like (some of my fav):
<ul>
	<li><a href="http://www.geocrawler.com/lists/3/SourceForge/18605/0/8531463/">move tabs, etc</a><br>
	<i>"Ok, after a suggestion from Rando, I renamed the functions in my
	patch to be a little more generic and not so horizontal-tabs
	specific (MoveTabPrev, MoveTabNext instead of MoveTabRight and
	MoveTabLeft). For those that don't remember, these two binds
	allow you to swap the focused tab with either the previous or next
	tab in the list, allowing you to move the tabs around in the list
	without touching the mouse."</i>
	<br>
	Author: Phil Dier | phil at gettcomm.com
	<br><br>

	<li><a href="http://www.geocrawler.com/lists/3/SourceForge/18605/0/8524524/">operate menus with keyboard</a><br>
	<i>
	"RootMenu' key binding is very useful, but I want to do all menu
	operation with keyboard. I have a try to implement this feature.
	With the patch at the end, you can use following bindings in your keys file (...)"
	</i>
	<br>
	Author: kita at kitaj.no-ip.com
	<br><br>

	<li><a href="http://www.geocrawler.com/lists/3/SourceForge/18605/0/8515478/">Sorted slit dockapps</a><br>
	<i>
	"This patch addresses the unpredictability of slit dockapp ordering.
	It stores the current order of dockapps in a file,
	default=~/.fluxbox/slitlist.  When loading dockapps into the slit it
	attempts to maintain the previous ordering, matching with
	previously-run dockapps by name."
	</i>
	<br>
	Author: Steve Cooper | stevencooper at isomedia.com
</ul>

To apply the patch, use:
<pre>
	# cd fluxbox-sources
	# patch -p0 < nameofthepatch.patch
</pre>
You can try different -p options like (-p1 or -p2) if something won't work.<br><br>
And there is more good stuff on <a href="http://lists.sourceforge.net/lists/listinfo/fluxbox-devel">Fluxbox-devel</a> mailing list,
take a look into <a href="http://www.geocrawler.com/redir-sf.php3?list=fluxbox-devel">archive</a>.<br>
If you want to subscribe, do it <a href="http://lists.sourceforge.net/lists/listinfo/fluxbox-devel">here</a>.




