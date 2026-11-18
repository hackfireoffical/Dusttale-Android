#!/usr/bin/env python3
"""Apply the small Android-native Dusttale chart patch to the upstream checkout."""
from pathlib import Path
import shutil
import sys

root = Path(sys.argv[1]).resolve()
here = Path(__file__).resolve().parents[1]
play = root / "source" / "PlayState.hx"
if not play.exists():
    raise SystemExit("Could not find upstream source/PlayState.hx")

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
print("Applied Android-native chart hooks and copied NativeDusttaleModcharts.hx")

# Keep the legacy game source compatible with the pinned modern HaxeFlixel API.
title = root / "source" / "TitleState.hx"
title_text = title.read_text(encoding="utf-8")
title_text = title_text.replace("import flixel.system.FlxSound;\\n", "")
title.write_text(title_text, encoding="utf-8")

main = root / "source" / "Main.hx"
main_text = main.read_text(encoding="utf-8")
main_text = main_text.replace("initialState, zoom, framerate, framerate, skipSplash", "initialState, Std.int(zoom), framerate, framerate, skipSplash")
main.write_text(main_text, encoding="utf-8")
