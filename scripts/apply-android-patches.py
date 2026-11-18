#!/usr/bin/env python3
"""Apply Android compatibility fixes to the upstream Dusttale source."""
from pathlib import Path
import shutil
import sys

root = Path(sys.argv[1]).resolve()
here = Path(__file__).resolve().parents[1]

play = root / "source" / "PlayState.hx"
if not play.exists():
    raise SystemExit("Could not find upstream source/PlayState.hx")

# HaxeFlixel 6 moved FlxSound from flixel.system to flixel.sound.
for source_file in (root / "source").rglob("*.hx"):
    source_text = source_file.read_text(encoding="utf-8")
    fixed = source_text.replace("flixel.system.FlxSound", "flixel.sound.FlxSound")
    if fixed != source_text:
        source_file.write_text(fixed, encoding="utf-8")

# The legacy constructor included a zoom parameter removed from current FlxGame.
main = root / "source" / "Main.hx"
main_text = main.read_text(encoding="utf-8")
main_text = main_text.replace(
    "new FlxGame(gameWidth, gameHeight, initialState, zoom, framerate, framerate, skipSplash, startFullscreen)",
    "new FlxGame(gameWidth, gameHeight, initialState, framerate, framerate, skipSplash, startFullscreen)"
)
main.write_text(main_text, encoding="utf-8")

# Polymod 1.8 pulls jsonpath/thx versions that do not compile together on this toolchain.
# The Android port does not load external mods; keep Polymod enabled on non-Android targets.
project = root / "Project.xml"
project_text = project.read_text(encoding="utf-8")
project_text = project_text.replace(
    '<haxelib name="polymod"/>',
    '<haxelib name="polymod" unless="android"/>'
)
project.write_text(project_text, encoding="utf-8")

# Preserve the existing Android-native receptor animation patch.
text = play.read_text(encoding="utf-8")
class_source = here / "source" / "NativeDusttaleModcharts.hx"
shutil.copy2(class_source, root / "source" / "NativeDusttaleModcharts.hx")

start_anchor = "\t\tgenerateStaticArrows(1);"
start_call = "\n\t\t#if android\n\t\tNativeDusttaleModcharts.start(curSong, strumLineNotes);\n\t\t#end"
if start_call not in text:
    if start_anchor not in text:
        raise SystemExit("Could not find startCountdown receptor initialization anchor")
    text = text.replace(start_anchor, start_anchor + start_call, 1)

update_anchor = "\t\t#if windows\n\t\tif (executeModchart && luaModchart != null && songStarted)"
update_call = "\t\t#if android\n\t\tif (songStarted) NativeDusttaleModcharts.update(curSong, Conductor.songPosition, Conductor.bpm, curStep, strumLineNotes);\n\t\t#end\n\n"
if update_call not in text:
    if update_anchor not in text:
        raise SystemExit("Could not find PlayState.update modchart anchor")
    text = text.replace(update_anchor, update_call + update_anchor, 1)

play.write_text(text, encoding="utf-8")
print("Applied FlxSound, FlxGame, Android Polymod, and native chart compatibility fixes")
