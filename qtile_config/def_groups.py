from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

def generate_groups() -> list:
    return [
    Group("", layout="monadtall",        matches=[Match(wm_class=["librewolf, brave-browser, firefox"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["qpdfview", "thunar", "nemo", "caja", "pcmanfm"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["jellyfinmediaplayer", "freetube"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["signal-desktop"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["keepassxc"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["vscodium"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["github"])]),
    Group("", layout="monadtall",        matches=[Match(wm_class=["github"])]),
# "   ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   "
]

# Group Key mappings   

def set_group_keys(groups:list, keys:list, mod_key:str) -> None:
    for i, group in enumerate(groups, start=1):
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod_key],
                    str(i),
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod_key, "shift"],
                    str(i),
                    lazy.window.togroup(group.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(group.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod_key, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )
