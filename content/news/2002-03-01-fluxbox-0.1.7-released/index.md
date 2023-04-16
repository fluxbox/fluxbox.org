---
title: |
  2002-03-01 19:54:00 - Fluxbox 0.1.7 Released!
author: "aleczapka"
date: "2002-03-01 19:54:00"
---

# Fluxbox 0.1.7 Released!

Yes, the next <a href="http://sourceforge.net/project/showfiles.php?group_id=35398&release_id=77568">release</a> is finally there!
<br><br>

What's new in 0.1.7:
<ul>
    <li>Title bar configuration is moved to the <code>init</code> file
    <li>Fluxbox will auto copy the default files to <code>~/.fluxbox/</code>  if they don't exist
    <li>Partial Gnome support:<br>
        Atoms supported:
        <ul type=square>
            <li>_WIN_WORKSPACE
            <li>_WIN_WORKSPACE_COUNT
            <li>_WIN_WORKSPACE_NAMES
            <li>_WIN_CLIENT_LIST
            <li>_WIN_STATE :
                <ul type=circle>
                    <li>WIN_STATE_MINIMIZED
                    <li>WIN_STATE_STICKY
                    <li>WIN_STATE_SHADED
                </ul>
            <li>_WIN_HINT:<br>
                WIN_HINTS_SKIP_FOCUS
        </ul>
    <br>

    <li>Tree new languages
        <ul type=square>
            <li>Portuguese
            <li>Bulgarian
            <li>Japanese
        </ul>
    <br>

    <li>New key bindings and with parameter support
        <ul type=square>
            <li>NudgeRight <step>
            <li>NudgeLeft <step>
            <li>NudgeUp <step>
            <li>NudgeDown <step>
            <li>PrevWorkspace <step>
            <li>NextWorkspace <step>
            <li>Workspace <workspacenum><br>
                <i>We keep the Workspace1 Workspace2 etc
                but they will be removed in next release</i>
            <li><b>new:</b> - LeftWorkspace<br>
                <i>This will change to the workspace to the left (no workspace cycling)</i>
            <li><b>new:</b> - RightWorkspace<br>
                <i>This will change to the workspace to the right (no workspace cycling)</i>
            <li><b>new:</b> - SendToWorkspace <workspacenum><br>
                <i>Sends current window to a workspace</i>
        </ul>
    <br>

    <li>Huge code clean up
</ul>

Bugfixes in 0.1.7:
<ul>
    <li>BadWindow error in ~FluxboxWindow
    <li>negative width in a window
    <li>Fixed lower/raise of windows when using windowmenu/keybinding so now tabs should follow
    <li>Slit always on top crash
</ul>

Don't wait any longer and <a href="http://sourceforge.net/project/showfiles.php?group_id=35398&release_id=77568">get it here</a>.



