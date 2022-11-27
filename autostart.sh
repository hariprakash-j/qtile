#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b

# Applying the wallpaper
nitrogen --restore

# Start up applications
nextcloud &
