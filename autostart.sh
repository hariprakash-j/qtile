#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b &

# Applying the wallpaper
nitrogen --restore

nextcloud &
protonmail-bridge --noninteractive &
gtk-launch webapp-Airsonic6135.desktop &
signal-desktop &
librewolf &
freetube &
thunderbird &
signal-desktop &
thunar &