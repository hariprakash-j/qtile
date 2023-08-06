#!/bin/sh
primary=DP-0
secondary=HDMI-0
tertiary=DP-1

if xrandr | grep "${secondary} connected primary"; then
    xrandr --output "${primary}" --auto --primary --output "${secondary}" --off
    echo "switched to ${primary}"
else if xrandr | grep "${primary} connected primary"; then
    xrandr --output "$secondary" --auto --primary --rotate right --output "${primary}" --off
    echo "switched to ${secondary}"
fi
fi