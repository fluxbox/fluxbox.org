# NAME

fbrun - display run dialog window

# SYNOPSIS

**fbrun** \[*options*\]

# DESCRIPTION

**fbrun(1)** is basically equivalent to the “Run…​” dialog in other
desktop environments. This means that it is an easy way to start a
program that isn’t contained in the menu (or needs a special set of
parameters for this particular invocation).

Pressing “Enter” will close the window and execute the command in your
present **$SHELL**. Pressing “Esc” will close the window and does not
execute anything.

Another way fbrun can be useful is to be called from the menu with a
preloaded command line that you can edit and then execute. An example
might be sshing to a very long host name with lots of options of which
one changes all the time. In this case, you could add an entry for fbrun
to your menu that contains all the options and the host name. When you
use said entry, you could edit the line as necessary and execute it.

# OPTIONS

**-title** *title*  
Set title

**-text** *text*  
Text input

**-w** *width*  
Window width in pixels

**-h** *height*  
Window height in pixels

**-display** *display*  
Display name, defaults to **$DISPLAY**

**-pos** *x* *y*  
Window position in pixels

**-nearmouse**  
Position the window under the mouse cursor

**-center**  
Position the window on the screen center

**-fg** *color*  
Foreground text color. The default is **black**

**-bg** *color*  
Background color. The default is **white**

**-font** *name*  
Text font name

**-hf** *filename*  
History file to load. The default is **~/.fluxbox/fbrun\_history**.

**-cf** *filename*  
Completion data to load. The default is empty. If no data can be loaded,
completion defaults to executables in $PATH

**-preselect**  
Select the preset text given by the **-text** parameter

**-autocomplete**  
Complete on typing. You can also set the FBRUN\_AUTOCOMPLETE environment
(to any value)

**-help**  
Show this help

# EXAMPLE

    fbrun -fg black -bg white -text xterm -title "run xterm"

# AUTHORS

This manpage was originally written by Bastian Kleineidam &lt;calvin at
debian.org&gt; for the Debian distribution of fluxbox (but may be used
by others).

It was then converted to asciidoc format by Jim Ramsay &lt;i.am at
jimramsay.com&gt; for fluxbox-1.1.2

# SEE ALSO

fluxbox(1)
