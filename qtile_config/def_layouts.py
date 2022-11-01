from libqtile import layout
from libqtile.config import Match
from .def_theme import colors

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 10
}

def generate_layouts() -> list():
    return [
        # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        # layout.MonadTall(),
        layout.Max(),
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        layout.MonadTall(**layout_conf),
        # layout.MonadWide(**layout_conf),
        # layout.Bsp(**layout_conf),
        # layout.Matrix(columns=2, **layout_conf),
        # layout.RatioTile(**layout_conf),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]

def generate_floating_layout():
    return layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
    )