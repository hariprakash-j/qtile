import subprocess

from libqtile.lazy import lazy


@lazy.function
def switch_audio(*args, **kwargs):
    HEADPHONES_NAME = "Starship/Matisse HD Audio Controller Analog Stereo"
    SPEAKERS_NAME = "GA102 High Definition Audio Controller Digital Stereo"

    audio_sources = [HEADPHONES_NAME, SPEAKERS_NAME]
    source_status = []
    for source in audio_sources:
        output_string = get_pipewire_status(source)
        source_status.append(output_string)
    for status in source_status:
        if "*" not in status:
            target_device_id = status.split(".")[0].split(" ")[-1]
            subprocess.run(f"wpctl set-default {target_device_id}", shell=True)


def get_pipewire_status(source):
    output = subprocess.Popen(
        f"wpctl status | grep '{source}'", shell=True, stdout=subprocess.PIPE
    )
    if output.stdout:
        return str(output.stdout.read())
