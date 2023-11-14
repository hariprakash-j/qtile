import subprocess
from libqtile import widget
from .def_theme import colors


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=6, padding=2)


def icon(fg="text", bg="dark", fontsize=18, text="?"):
    return widget.TextBox(**base(fg, bg), fontsize=fontsize, text=text, padding=1)


def powerline(fg="light", bg="dark"):
    return widget.TextBox(**base(fg, bg), text="", fontsize=50, padding=-6)  # Icon: nf-oct-triangle_left


def powerline_reverse(fg="light", bg="dark"):
    return widget.TextBox(**base(fg, bg), text="", fontsize=30, padding=-1)  # Icon: nf-oct-triangle_right


def switch_audio():
    HEADPHONES_ID = "43"
    SPEAKERS_ID = "42"
    output = subprocess.Popen("wpctl status | grep '*'", shell=True, stdout=subprocess.PIPE)
    output_string = str(output.stdout.read())
    if SPEAKERS_ID in output_string:
        subprocess.run(f"wpctl set-default {HEADPHONES_ID}", shell=True)
    else:
        subprocess.run(f"wpctl set-default {SPEAKERS_ID}", shell=True)


def workspaces():
    return [
        widget.GroupBox(
            **base(fg="light"),
            fontsize=17,
            margin_y=3,
            margin_x=3,
            padding_y=2,
            padding_x=2,
            borderwidth=3,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            disable_drag=True,
        ),
        powerline_reverse("color2", "dark"),
        separator(),
        widget.WindowName(**base(fg="focus"), fontsize=15, padding=2),
        separator(),
    ]


primary_widgets = [
    widget.CurrentLayoutIcon(**base(bg="dark", fg="light")),
    separator(),
    *workspaces(),
    separator(),
    powerline("color2", "dark"),
    powerline("dark", "color2"),
    widget.Memory(**base(bg="dark", fg="light"), measure_mem="G"),
    powerline("color2", "dark"),
    widget.CPU(**base(bg="color2", fg="dark"), format="{freq_current}GHz {load_percent}%"),
    powerline("dark", "color2"),
    icon(bg="dark", fg="light", text=" "),  # Icon: nf-fae-sun_cloud
    widget.Wttr(**base(bg="dark", fg="light"), location={"Bangalore": "Bangalore"}, format="%t"),
    powerline("color2", "dark"),
    widget.Net(**base(bg="color2"), prefix="M", interface="enp6s0", format="{down:.3f}{down_suffix} ↓↑ {up:.3f}{up_suffix}"),
    powerline("dark", "color2"),
    icon(bg="dark", fg="light", text=" "),
    widget.Volume(**base(bg="dark", fg="light"), step=1, mouse_callbacks={"Button3": switch_audio}),
    powerline("color2", "dark"),
    widget.Clock(**base(bg="color2"), format="%A %d/%m - %H:%M"),
    powerline("dark", "color2"),
    widget.Systray(background=colors["dark"], padding=5),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline("color2", "dark"),
    powerline("dark", "color2"),
    icon(bg="dark", fg="light", text=" "),  # Icon: nf-fae-sun_cloud
    widget.Volume(**base(bg="dark", fg="light"), step=1),
    powerline("color2", "dark"),
    widget.Clock(**base(bg="color2"), format="%A %d/%m - %H:%M"),
]
