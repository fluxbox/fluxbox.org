# NAME

fluxbox-remote - command line access to key commands for fluxbox(1)

# SYNOPSIS

**fluxbox-remote** *command*

# DESCRIPTION

*fluxbox-remote(1)* is designed to allow scripts to execute most key
commands from *fluxbox(1)*. *fluxbox-remote(1)* will only work with
*fluxbox(1)*: its communications with *fluxbox(1)* are not standardized
in any way. It is recommended that a standards-based tool such as
*wmctrl(1)* be used whenever possible, in order for scripts to work with
other window managers.

# CAVEATS

*fluxbox-remote(1)* uses the X11 protocol to communicate with
*fluxbox(1)*. Therefore, it is possible for any user with access to the
*X(7)* server to use *fluxbox-remote(1)*. For this reason, several key
commands have been disabled. Users should be aware of the security
implications when enabling *fluxbox-remote(1)*, especially when using a
forwarded *X(7)* connection.

# RESOURCES

session.screen0.allowRemoteActions: &lt;boolean&gt;  
This resource in ~/.fluxbox/init must be set to “true” in order for
*fluxbox-remote(1)* to function. Please read the **CAVEATS** first.

# ENVIRONMENT

In order to communicate with *fluxbox(1)*, the DISPLAY environment
variable must be set properly. Usually, the value should be “:0.0”.

# AUTHORS

This man page written by Mark Tiefenbruck &lt;mark at fluxbox.org&gt;

# SEE ALSO

fluxbox(1) fluxbox-keys(5) wmctrl(1)
