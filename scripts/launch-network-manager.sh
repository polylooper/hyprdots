#!/bin/bash

# Check if nmgui is already running
if pgrep -x nmgui >/dev/null; then
    # Focus the existing window using Hyprland
    hyprctl dispatch focuswindow "class:nmgui"
else
    # Start nmgui as floating
    nmgui &
fi

