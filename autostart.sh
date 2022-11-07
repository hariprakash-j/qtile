#!/bin/bash

# Disabling display auto off
xset s off -dpms

sleep 1s

# Starting the compositor
picom -b

# Applying the wallpaper
nitrogen --restore

# Start up applications
nextcloud &
