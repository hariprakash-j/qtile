#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b &

# Applying the wallpaper
nitrogen --restore

nextcloud &
gtk-launch webapp-Airsonic6135.desktop &
signal-desktop &
librewolf &
freetube &
signal-desktop &
thunar &

# launching the proton bridge and thunderbird after a delay
protonmail-bridge --noninteractive &
sleep 10
thunderbird &