from libqtile import hook
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy
import subprocess, os, socket
import shutil

from qtile_config import def_keys, def_groups, def_layouts, def_screens, def_mouse

mod_key = "mod4"
terminal = "alacritty"

# Configuring Keys
keys = def_keys.generate_keys(mod_key, terminal)

# Configuring Groups and setting Keys for the groups
groups = def_groups.generate_groups()
def_groups.set_group_keys(groups, keys, mod_key)

# Configuring Layouts and Drag floating layouts.
layouts = def_layouts.generate_layouts()
floating_layout = def_layouts.generate_floating_layout()

# Configuring Screens
screens = def_screens.screens
widget_defaults = {
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 14,
    "padding": 2,
}

# Configuring Mouse actions
mouse = def_mouse.generate_mouse(mod_key)


# Configuring hooks
# Autostart programs
@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([autostart_script])


@hook.subscribe.restart
def restart_cleanup():
    shutil.rmtree(os.path.expanduser("~/.config/qtile/__pycache__"))


@hook.subscribe.shutdown
def shutdown_cleanup():
    shutil.rmtree(os.path.expanduser("~/.config/qtile/__pycache__"))


# Other Options
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
