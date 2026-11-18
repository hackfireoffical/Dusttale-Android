# Android port audit — 18 November 2026

## Upstream baseline

- Base project: TheoDeveloping/Dusttale-Android-Port (Kade Engine-derived Android project).
- Android orientation is landscape and fullscreen in Project.xml.
- Android touch-control implementation is under source/android/.
- The inspected upstream checkout contains the original game asset bundle; this repository does not redistribute those assets.
- All 36 chart JSON files parsed successfully.
- The engine already includes Dust-specific note rendering and dedicated gameplay effects.
- Three non-empty built-in song modcharts were identified: Hallucinations, Reality Check, and Last Hope.

## Android compatibility patch

- Added source/NativeDusttaleModcharts.hx to reproduce the built-in receptor-motion sequences in Haxe.
- Added scripts/apply-android-patches.py to copy the class into an upstream checkout and inject Android-only start/update hooks.
- The GitHub Actions workflow checks out the upstream source and applies this patch before compiling.
- This is a targeted native implementation of the three identified sequences, not a general Lua runtime. In-game timing and visual parity still need verification.

## Build status

- A GitHub Actions Android build workflow is now included.
- The first successful APK build has not yet been confirmed.
- No claim of a completed or tested APK should be made until an artifact exists and is checked on a device.
