#!/bin/bash

# Disabling display auto off
xset s off -dpms

sleep 1s

# Applying the wallpaper
nitrogen --restore

# Start up applications
nextcloud &
