# Port audit — 18 November 2026

## Verified in the inspected upstream checkout

- Project: TheoDeveloping/Dusttale-Android-Port.
- Android orientation is landscape and fullscreen in Project.xml.
- Android touch-control code exists under source/android/.
- The upstream checkout includes the Dusttale game asset bundle; this project does not redistribute it.
- 36 chart JSON files parsed successfully.
- The engine already contains Dust-specific note rendering and dedicated gameplay effects.
- Ten song folders contain modchart.lua files. Most are empty callback stubs; three contain actual receptor motion: Hallucinations, Reality Check, and Last Hope.

## Android chart compatibility work added here

- Added source/NativeDusttaleModcharts.hx with Haxe-native implementations for the three non-empty built-in receptor-motion scripts.
- Added scripts/apply-android-patches.py, which copies the class into a clean upstream checkout and injects Android-only start/update hooks.
- The GitHub Actions workflow applies this patch before attempting the Android build.
- This is a targeted port of the three non-empty built-in scripts, not general Lua support. Visual and timing parity still requires in-game testing.

## Build status

- Initial build attempt failed because the runner's current Android SDK command-line tools require JDK 17, while the first workflow used JDK 11.
- The next workflow revision moved to JDK 17 and removed the obsolete SDK package named "tools".
- The latest build attempt is in progress. No APK is confirmed yet.
