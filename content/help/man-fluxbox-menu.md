---
weight: 4
---
# NAME

fluxbox-menu - fluxbox(1) menu syntax

# SYNOPSIS

@pkgdatadir@/menu

~/.fluxbox/menu

~/.fluxbox/windowmenu

# SYNTAX

Variable parameters are shown in emphasis: *argument*

All other characters shown are required verbatim. Whitespace is only
required to delimit words, but it is fine to add more whitespace.

# DESCRIPTION

There are two types of menus in fluxbox which can be configured.

The first is the root menu, which normally appears when you right-click
on the desktop.

The first is the **ROOT MENU** (Or right-click menu), is usually bound
to a right-click on the desktop, though this binding can be changed in
the “keys” file (**fluxbox-keys(5)**). This same syntax is used for the
**CustomMenu** command, also mentioned in **fluxbox-keys(5)**.

Fluxbox installs a default root menu file in **@pkgdatadir@/menu**. You
can also use fluxbox -i to confirm this location. Of course this
system-wide menu can be customized for all users at once, but it is also
possible to create an individual menu file for each user. By convention,
users create a menu file in **~/.fluxbox/menu**. Once you’ve created
your own menu file, you’ll want to make sure that you properly declare
this location in your “init” file so that fluxbox knows where to look.
See **RESOURCES**, below for details.

The second type is the **WINDOW MENU**, which defines the contents of
the menu which appears when you right-click on a window’s titlebar or
iconbar. This opens a menu file as defined by **~/.fluxbox/windowmenu**.
If this file does not exist, fluxbox will copy in the default from
**@pkgdatadir@/windowmenu**.

You do not need to “reload” fluxbox after editing either menu file, the
changes should be taken into account the next time you open the menu.

# ROOT MENU

The root menu must begin with a **\[begin\]** tag and end with an
**\[end\]** tag, and every tag must be on its own line.

There are up to four fields in a menu line. They are of the form
\[*tag*\] (*label*) {*command*} &lt;'icon'&gt;

The &lt;'icon'&gt; field is always optional when shown below. If
specified, the *icon* will be scaled down and displayed in the menu
alongside the text label of the item. It must be in .xpm or .png format.

Any line that starts with a *\#* or *!* is considered a comment and
ignored by fluxbox. Also, in the label/command/filename fields you can
escape any character. Using *\\* inserts a literal back-slash into the
label/command/filename field.

You may enter labels, commands, and icons using characters from any
**iconv(1)** language/locale by specifying the encoding used via the
**\[encoding\]** tag, detailed below.

## Structural Tags

**\[begin\]** (*title*)
This tells fluxbox to start parsing the menu file. This tag is required
for fluxbox to read your menu file. If it cannot find it, the system
default menu is used in its place. The *title* appears at the top of the
menu. And **\[end\]** tag is required to end the menu.

**\[submenu\]** (*label*) {*title*} &lt;'icon'&gt;
This tells fluxbox to create and parse a new menu, which is inserted as
a submenu into the parent menu. These menus are parsed recursively, so
there is no limit to the number of levels or nested submenus you can
have. The *label* is the text that will appear in the parent menu, and
the *title* is shown at the top of the submenu. If omitted, the *title*
will be the same as the *label*. An **\[end\]** tag is required to end
the submenu.

**\[end\]**
This tells fluxbox that it is at the end of a menu. This can either be a
**\[submenu\]** or the **\[begin\]** tag of the main root menu. There
must be at least one of these tags in your menu to correspond to the
required **\[begin\]** tag, and one for each **\[submenu\]**.

**\[encoding\]** {*encoding*}
This begins an **\[encoding\]** section and specifies the string
encoding of all strings until the matching **\[endencoding\]** tag. For
a list of available encodings on your system, run **iconv -l**.

**\[endencoding\]**
This ends an **\[encoding\]** section.

**\[include\]** (*path*)
Parses the file specified by filename inline with the current menu. The
*path* can be the full path to a file or it can begin with **~/**, which
will be expanded into your home directory. If *path* is a directory,
then all files in that directory are included.

**\[separator\]**
This will create a nice separation line. Useful for splitting up
sections in a “pretty” way. The optional *comment* is not displayed, but
can be useful for internal documentation or script parsing of menu
files.

**\[nop\]** (*label*) &lt;'icon'&gt;
Insert a non-operational item into the current menu. This is much like
**\[separator\]**, but instead of a line, it inserts a *label*. This can
be used to help format the menu into blocks or sections if so desired.
The *label* is optional, and if omitted a blank item will be inserted.

## Applications

**\[exec\]** (*label*) {*command…​*} &lt;'icon'&gt;
Inserts a command item into the menu. When you select the menu item from
the menu, fluxbox runs *command…​* in your **$SHELL** (or /bin/sh if
$SHELL is not set). You can use this to launch applications, run shell
scripts, etc. Since all arguments are passed verbatim to the shell, you
can use environment variables, pipes, or anything else the shell can do.
Note that processes only see environment variables that were set before
fluxbox started (such as in ~/.fluxbox/startup).

## Fluxbox Functions

**\[config\]** (*label*) &lt;'icon'&gt;
Inserts a fluxbox native submenu item, containing numerous configuration
options concerning window placement, focus style, window moving style,
etc. See **Configuration Menu** in **fluxbox(1)** for details.

**\[reconfig\]** (*label*) &lt;'icon'&gt;
When selected this item re-reads the current style and menu files and
applies any changes. This is useful for creating a new style or theme,
as you don’t have to constantly restart fluxbox every time you save your
style. However, fluxbox automatically rereads the menu whenever it
changes.

**\[restart\]** (*label*) {*command*} &lt;'icon'&gt;
This tells fluxbox to restart. If *command* is supplied, it shuts down
and runs the command (which is commonly the name of another window
manager). If *command* is omitted, fluxbox restarts itself.

**\[exit\]** (*label*) &lt;'icon'&gt;
Inserts an item that shuts down and exits fluxbox. Any open windows are
reparented to the root window before fluxbox exits.

**\[style\]** (*label*) {*filename*} &lt;'icon'&gt;
This tells fluxbox to insert an item that, when selected, reads style
file named filename and apply the new textures, colors and fonts to the
current running session.

**\[stylesmenu\]** (*directory*) &lt;'icon'&gt;
Reads all filenames from the specified directory, assuming that they are
all valid style files, and creates inline menu items in the current menu
for every filename, that, when selected by the user will apply the
selected style file to the current session. The labels that are created
in the menu are the filenames of the style files.

**\[stylesdir\]** (*label*) {*directory*} &lt;'icon'&gt;
Creates a submenu entry with *label* (that is also the title of the new
submenu), and inserts in that submenu all filenames in the specified
*directory*, assuming that they are all valid style files (directories
are ignored) in the same way as the **\[stylesdir\]** command does. Both
**\[stylesdir\]** and **\[stylesmenu\]** commands make it possible to
install style files without editing your init file.

**\[wallpapers\]** (*directory*) {*command*} &lt;'icon'&gt;
This inserts a menu item to set the wallpaper for each file in the given
directory. The *command* is optional, and defaults to **fbsetbg**.

**\[workspaces\]** (*label*) &lt;'icon'&gt;
This tells fluxbox to insert a link to the workspaces menu directly into
your menu. See **Workspace Menu** in **fluxbox(1)** for details.

**\[***command***\]** (*label*) &lt;'icon'&gt;
In addition to the commands above, any legal keys file *command* may be
used as a menu item. See **fluxbox-keys(5)** for more information.

# WINDOW MENU

The syntax for the Window Menu is mostly identical to that for the
**ROOT MENU**; it must start with **\[begin\]** and end with
**\[end\]**, and may have any of the above tags. However, it may also
contain any of the following window-specific **\[***tag*\*\]\*s, which
each must be on a line by itself with no labels, commands, or icons.

The additonal available tags in this menu are:

**\[shade\]**
Provides a menu item to shade or unshade (or, roll-up) the window. This
is equivalent to the shade titlebar button.

**\[stick\]**
Provides a menu item to stick or unstick the window. Stuck windows are
displayed on all workspaces. This is equivalent to the stick titlebar
button.

**\[maximize\]**
Provides a menu item to maximize or unmaximize the window, equivalent to
the maximize titlebar button. The button with which you click alters the
behaviour of this item as follows:

-   Button 1 (Un)Maximize as normal.

-   Button 2 (Un)Maximize window vertically.

-   Button 3 (Un)Maximize window horizontally.

**\[iconify\]**
Provides a menu item to iconify (or, minimize) the window, equivalent to
the iconify titlebar button.

**\[close\]**
Closes the window gracefully, equivalent to the titlebar button.

**\[kill\]**
Kills the window’s process, like **xkill(1)**.

**\[raise\]**
Raise the window to the top of the stack within its layer.

**\[lower\]**
Lower the window to the bottom of the stack within its layer.

**\[settitledialog\]**
Opens a dialog which can be used to set the window’s title. Some
applications may re-set their own title from time-to-time, wiping out
your setting.

**\[sendto\]**
Sends the window to a different workspace. When you select the workspace
with a middle-click, fluxbox will also change to the new workspace. A
regular click only sends the window.

**\[layer\]**
Adds a “Layer…​” submenu which lets you change the layer of this window.

**\[alpha\]**
Adds a “Transparency…​” submenu which lets you change the focused and
unfocused transparency of this window.

**\[extramenus\]**
Adds the “Remember…​” menu item, which allows you to specify which
settings should be stored in the “apps” file (See **fluxbox-apps(5)**
for more details).

**\[separator\]**
Adds a horizontal line to the menu

# FILES

**~/.fluxbox/menu**
This is the default location for the user’s root menu.

**@pkgdatadir@/menu**
This is the system-wide root menu file. It will be used if the user’s
root menu is missing or unparseable.

**~/.fluxbox/windowmenu**
This is the user’s window menu definition file

**@pkgdatadir@/menu**
This is the default window menu. If the user does not have this file, it
will be copied to **~/.fluxbox/windowmenu** on fluxbox startup.

# RESOURCES

**session.menuFile:** *location*
This may be set to override the location of the user’s root menu.

# ENVIRONMENT

The *comand…​* field of the **\[exec\]** tag can take advantage of other
environment variables if they are set before fluxbox is started.

# EXAMPLES

**Root Menu**

    # fluxbox menu file
    [begin] (fluxbox)
        [exec] (rxvt) {rxvt -ls} </usr/X11R6/share/icons/terminal.xpm>
        [exec] (netscape) {netscape -install}
        [exec] (The GIMP) {gimp}
        [exec] (XV) {xv}
        [exec] (Vim) {rxvt -geometry 132x60 -name VIM -e screen vim}
        [exec] (Mutt) {rxvt -name mutt -e mutt}
        [submenu] (mozilla)
            [exec] (browser) {mozilla -browser}
            [exec] (news) {mozilla -news}
            [exec] (mail) {mozilla -mail}
            [exec] (edit) {mozilla -edit}
            [exec] (compose) {mozilla -compose}
        [end]
        [submenu] (Window Manager)
            [exec] (Edit Menus) {nedit ~/.fluxbox/menu}
            [submenu] (Style) {Which Style?}
                [stylesdir] (~/.fluxbox/styles)
                [stylesmenu] (fluxbox Styles) {@pkgdatadir@/styles}
            [end]
            [config] (Config Options)
            [reconfig] (Reconfigure)
            [restart] (Restart)
        [end]
        [exit] (Log Out)
    [end]

**Default Window Menu**

    [begin]
      [shade]
      [stick]
      [maximize]
      [iconify]
      [raise]
      [lower]
      [settitledialog]
      [sendto]
      [layer]
      [alpha]
      [extramenus]
      [separator]
      [close]
    [end]

# AUTHORS

-   Jim Ramsay &lt;i.am at jimramsay com&gt; (&gt;fluxbox-1.0.0)

-   Curt Micol &lt;asenchi at asenchi com&gt; (&gt;fluxbox-0.9.11)

-   Tobias Klausmann &lt;klausman at users sourceforge net&gt;
    (⇐fluxbox-0.9.11)

-   Grubert &lt;grubert at users sourceforge net&gt; (fluxbox)

-   Matthew Hawkins &lt;matt at mh dropbear id au&gt; (blackbox)

-   Wilbert Berendsen &lt;wbsoft at xs4all nl&gt; (blackbox)

# SEE ALSO

fluxbox(1) fluxbox-keys(5) fluxbox-apps(5) xkill(1) iconv(1)
