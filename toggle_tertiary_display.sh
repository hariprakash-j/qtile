#!/bin/sh

primary=DP-0
secondary=HDMI-0
tertiary=DP-1

if xrandr | grep "${tertiary} connected 1920x1080"; then
    xrandr --output "${tertiary}" --off
    echo "turned on ${tertiary}"
else
    xrandr --output "${tertiary}" --auto --right-of "${secondary}"
    echo "switched to ${tertiary}"
fi
fi