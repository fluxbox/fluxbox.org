# NAME

fbsetbg - Set a background wallpaper or pattern

# SYNOPSIS

**fbsetbg** \[**-uU** *wallpapersetter*\] \[**-fFcCtTaA**\] *wallpaper*

**fbsetbg** \[**-uU** *wallpapersetter*\] **-rR** *path*

**fbsetbg** **-bB** *fbsetrootoptions…​*

**fbsetbg** \[-**l**|**h**|**i**|**p**\]

# DESCRIPTION

**fbsetbg(1)** is a wrapper that tries to find a suitable
background-setting app and then tries to set the wallpaper using that
app. You don’t have to configure fbsetbg. It just uses the first app it
can find.

Furthermore it supports remembering the last set wallpaper so you don’t
have to edit the style or init-file to change the wallpaper.

It aims to provide clear error messages in a window that make debugging
problems easy.

# OPTIONS

**-f** *file*  
Set fullscreen wallpaper.

**-c** *file*  
Set centered wallpaper.

**-t** *file*  
Set tiled wallpaper.

**-a** *file*  
Set maximized wallpaper, preserving aspect (if your bgsetter doesn’t
support this option fbsetbg falls back to **-f**).

**-u** *wallpapersetter*  
Use specified wallpapersetter, use no argument to forget.

**-b** *fbsetrootoptions*  
Forward the options to **fbsetroot(1)**. These can be used to set a
solid, pattern, or gradient background texture.

**-r** *directory*  
Set random wallpaper from a directory.

**-F**, **-C**, **-T**, **-A**, **-U**, **-B**, **-R**  
Same as the lowercase option but without remembering.

**-l**  
Set previous wallpaper. Or, if the random feature was last used, set
another random wallpaper from the same directory.

**-i**  
Display useful information about best wallpapersetter found.

**-p**  
Display some useful tips.

**-h**  
Display a help message.

# FILES

**~/.fluxbox/lastwallpaper**  
In this file the wallpaper you set will be stored, for the **-l**
option.

# ENVIRONMENT

**wpsetters**  
Wallpapersetters to use. This can be a space-delimited list of the
applications to try, or just a single name.

**DISPLAY**  
The display you want to set the wallpaper on.

# EXAMPLES

To use **feh(1)** as wallpapersetter and set **wallpapper.jpg** from the
current directory as wallpaper.

    $ wpsetters=feh fbsetbg wallpaper.jpg

Recall the last set wallpaper on display **:0.0** with the stored
options.

    $ DISPLAY=:0.0 fbsetbg -l

# BUGS

**fbsetbg(1)** is not foolproof.

# AUTHORS

The author of fbsetbg is Han Boetes &lt;han at fluxbox.org&gt;

This manpage was converted to asciidoc format by Jim Ramsay &lt;i.am at
jimramsay.com&gt; for fluxbox-1.1.2

# SEE ALSO

fluxbox(1) fbsetroot(1)
