# NAME

fbsetroot - a simple background utility used by the fluxbox(1) window
manager, originally written for and by the original blackbox(1) window
manager.

# SYNOPSIS

**fbsetroot** \[-display *display*\] -solid *color*

**fbsetroot** \[-display *display*\] -mod *x* *y* -fg *color* -bg
*color*

**fbsetroot** \[-display *display*\] -gradient *texture* -from *color*
-to *color*

**fbsetroot** -help

# DESCRIPTION

**fbsetroot(1)** is a utility that can control the appearance of the
root window in three ways: Either give it a solid color, or write a two
color modula pattern to it, or render a gradient texture, based on two
different colors.

fbsetroot resembles **xsetroot(1)** in this functionality but it
supports multiple-screen displays, and gradient textures the same way as
blackbox or fluxbox does. It doesn’t handle cursors etc. fbsetroot was
originally part of the Blackbox package and was carried over with the
code that became Fluxbox. It was called bsetroot back in those days.

If any errors are encountered, fbsetroot will use either
**gxmessage(1)** or **xmessage(1)** to inform the user of errors.

# OPTIONS

fbsetroot operates in three ways, you must choose one of the first 3
options:

**-solid** *color*  
Sets the root window to specified color.

**-mod** *x* *y*  
Creates a modula pattern. You must specify **-bg** and **-fg** colors.

**-gradient** *texturestring*  
Renders the specified texture string to the root window.

*texturestring* may be one of:  
**Horizontal / Vertical / Diagonal / Crossdiagonal / Pipecross /
Elliptic / Rectangle / Pyramid**

Select one of these texture types, they only apply when **-gradient** is
specified. You must also specify both a **-from** and a **-to** color.

**-display** *display*  
Tells fbsetroot to connect to the specified display.

**-bg, -background** *color*  
Background color. Needed for **-mod** patterns.

**-fg, -foreground** *color*  
Foreground color. Needed for **-mod** patterns.

**-from** *color*  
Start color for rendering textures. Needed for **-gradient** patterns.

**-to** *color*  
Ending color for rendering textures. Needed for **-gradient** patterns.

**-help**  
Prints version info and short help text.

# AUTHORS

This manpage was modified by Curt "Asenchi" Micol &lt;asenchi at
asenchi.com&gt; for the Fluxbox window manager.

Further updates for fluxbox-1.1.2 and conversion to asciidoc format by
Jim Ramsay &lt;i.am at jimramsay.com&gt;

# SEE ALSO

fluxbox(1) fbsetbg(1) xsetroot(1) xmessage(1) gxmessage(1)
