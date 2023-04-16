---
title: |
  2003-11-14 14:15:00 - Fluxbox and gnome-settings-daemon (SOLVED)
author: "aleczapka"
date: "2003-11-14 14:15:00"
---

# Fluxbox and gnome-settings-daemon (SOLVED)

Several people have sent info about <a href="http://www.muhri.net/nav.php3?node=gts">gtk+/gtk2 theme switcher</a>, which does exacly the job. <a href="mailto:fopref&#64;lanrules.de">Johannes Jordan</a> wrote a very helpfull answer:
<blockquote>
As asked for in the news, I want to give you a hopefully helping answer.
<br><br>

I think what you mean is how to select a nice looking theme for gtk+(2)
without gnome 2. themes are everything about the look of gtk+.
<br><br.

There is a tool called Gtk Theme Switch. It's website is
<a href="http://www.muhri.net/nav.php3?node=gts">http://www.muhri.net/nav.php3?node=gts</a>.
<br><br>

It works in the command line but also has a nice minimalistic GUI.
<br><br>

It is available as 'gtk-theme-switch' debian package. In the testing and
the unstable branch, it is already up to date and capable of switching
gtk2 themes (command switch2 for this). in stable branch, there is an
older version only supporting gtk1.
<br><br>

If you want to do it yourself, you can edit the .gtkrc-2.0 file in your
home directory. it can be written like a theme file (every gtk theme is
a gtkrc file, most themes use a so called theme engine - the gtkrc
file tells to load the specific lib) and it can also have an include
command for the gtkrc of an installed theme. mine look like follows:
<pre>
# --
include "/usr/share/themes/ThinIce/gtk-2.0/gtkrc"
# --
</pre>
<br>

There IS another command available to load themes (telling only the name
without the path etc., i.e. "ThinIce"), but I can't remember it now.
<br><br>

If you want to change stuff declared (or even not declared) in the
theme's gtkrc without editing the theme (which could be overwritten on
updates etc) you can add this to your .gtkrc-2.0 after the include as
well. good thing for using another font...
<br><br>
</blockquote>

<a href="mailto:roman&#64;isoTree.com">Roman Meytin</a> adds: You
If you use gentoo you can <code>'emerge x11-themes/gtk-theme-switch'</code>.
You can also use 'qtconfig,' which I believe comes with QT to perform
similar actions on QT/KDE applications.
<br><br>
Thanks all for the quick answers.



