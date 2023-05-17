#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b &

# Applying the wallpaper
nitrogen --restore

flatpak run com.nextcloud.desktopclient.nextcloud &
protonmail-bridge --noninteractive &
gtk-launch webapp-Airsonic6135.desktop &
signal-desktop &
mullvad-browser &
flatpak run io.freetubeapp.FreeTube &
thunderbird &
flatpak run org.signal.Signal &
pcmanfm &