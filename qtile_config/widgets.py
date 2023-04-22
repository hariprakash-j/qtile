from libqtile import widget
from .def_theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=2)


def icon(fg='text', bg='dark', fontsize=18, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=-6
    )


def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            fontsize=15,
            margin_y=3,
            margin_x=3,
            padding_y=9,
            padding_x=9,
            borderwidth=0,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=15, padding=2),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color2', 'dark'),

    powerline('dark', 'color2'),

    widget.Memory(**base(bg='dark', fg='light'), measure_mem='G'),

    powerline('color2', 'dark'),

    widget.CPU(**base(bg='color2', fg='dark'), format='{freq_current}GHz {load_percent}%'),

    powerline('dark', 'color2'),

    icon(bg="dark", fg="light", text=' '),

    widget.Volume(**base(bg='dark', fg='light'), step=1),

    powerline('color2', 'dark'),
    
    widget.Net(**base(bg='color2'), prefix='M', interface='enp6s0', format='U:{up} D:{down}'),

    powerline('dark', 'color2'),

    icon(bg="dark", fg='light', text=' '), # Icon: nf-fae-sun_cloud

    widget.Wttr(**base(bg='dark', fg='light'), location={'Bangalore': 'Bangalore'}, format="%t"),

    powerline('color2', 'dark'),

    widget.Clock(**base(bg='color2'), format='%A %d/%m - %H:%M'),

    powerline('dark', 'color2'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color2', 'dark'),

    powerline('dark', 'color2'),
    
    icon(bg="dark", fg='light', text=' '), # Icon: nf-fae-sun_cloud

    widget.Wttr(**base(bg='dark', fg='light'), location={'Bangalore': 'Bangalore'}, format="%t"),

    powerline('color2', 'dark'),

    widget.Clock(**base(bg='color2'), format='%A %d/%m - %H:%M'),

]

