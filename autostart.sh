#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b --backend xrender &

# Applying the wallpaper
nitrogen --restore

signal-desktop &

# launching the proton bridge and thunderbird after a delay
protonmail-bridge --noninteractive &
sleep 10
thunderbird &
