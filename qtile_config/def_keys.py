from libqtile.lazy import lazy
from libqtile.config import Key


def generate_keys(mod_key:str, terminal:str) -> list:
    return [
        # Switch between windows
        Key([mod_key], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod_key], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod_key], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod_key], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod_key], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod_key, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod_key, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod_key, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod_key, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod_key, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod_key, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod_key, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod_key, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod_key], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # Volume control with volume button
        Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -2%"
        )),
        Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +2%"
        )),
        Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )),
        
        # Toggle between different layouts as defined below
        Key([mod_key], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod_key], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod_key, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod_key, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

        # Switch Displays
        Key([mod_key], "p", lazy.spawn("sh '/home/hari/.config/qtile/switch_display.sh'"), desc="Switch displays"),
        Key([mod_key, "shift"], "p", lazy.spawn("sh '/home/hari/.config/qtile/all_displays.sh'"), desc="Turn on all displays"),
        Key([mod_key], "period", lazy.next_screen(), desc='Next monitor'),

        # App Shortcut
        Key([mod_key, "shift"], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
        Key([mod_key], "u", lazy.spawn("thunar"), desc="Launch nemo, the file manager"),
        Key([mod_key], "i", lazy.spawn("flatpak run io.gitlab.librewolf-community"), desc="Launch librewolf, the web browser"),
        Key([mod_key], "y", lazy.spawn("flatpak run io.freetubeapp.FreeTube"), desc="Launch Freetube, the youtube client"),

        #Lock and sleep shortcuts
        Key([mod_key, "shift"], "Escape", lazy.spawn("systemctl suspend")),
        Key([mod_key, "control"], "Escape", lazy.spawn("systemctl poweroff")),
        Key([mod_key], "Escape", lazy.spawn("betterlockscreen -l")),

        # Rofi shortcuts
        Key([mod_key], "Return", lazy.spawn("rofi -show combi"), desc="Launch rofi"),
        Key([mod_key], "c", lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"), desc="Launch rofi calculator"),

        # Screenshot shortcuts
        Key([mod_key], "Print", lazy.spawn("flameshot screen --path /home/hari/Pictures"), desc="Take a screenshot of the entire active monitor"),
        Key([mod_key], "Print", lazy.spawn("flameshot gui --path /home/hari/Pictures"), desc="Take a screenshot of the entire active monitor"),
        
    ]
