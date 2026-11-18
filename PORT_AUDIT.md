# Port audit — 18 November 2026

## Verified in the inspected upstream checkout

- Project: TheoDeveloping/Dusttale-Android-Port.
- Android orientation is landscape and fullscreen in Project.xml.
- Android touch-control code exists under source/android/.
- The checkout contained the Dusttale asset bundle; this project does not redistribute it.
- 36 chart JSON files parsed successfully.
- The engine already has custom note-type rendering and dedicated gameplay effects.

## Critical fidelity gap

PlayState currently discovers song modcharts only under `#if windows`. ModchartState and its Lua bindings are also Windows-gated, and linc_luajit is declared for Windows only. Therefore Android does not execute the song Lua modcharts. Removing the guard alone would not work. The missing behaviors need an Android-compatible Lua runtime or native Haxe ports, then song-by-song validation.

## Build status

The source inspection and chart validation were completed. An Android APK build has not yet been completed or tested. The Actions workflow in this repository is an initial reproducible build attempt, not a claim of a working APK.
