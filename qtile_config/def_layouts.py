from libqtile import layout
from libqtile.config import Match
from .def_theme import colors

layout_conf = {"border_focus": colors["focus"][0], "border_width": 4, "margin": 10}


def generate_layouts() -> list:
    return [
        layout.Max(),
        layout.MonadTall(**layout_conf),
        layout.VerticalTile(**layout_conf),
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
