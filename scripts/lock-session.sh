#!/bin/bash
# Get current wallpaper
WALLPAPER=$(swww query | grep -oP 'image: \K.*' | head -n1)

# Resize to monitor resolution to avoid memory issues
convert "$WALLPAPER" -resize 3840x1600\> ~/.config/matugen/templates/current_wallpaper.jpg

# Lock
hyprlock
