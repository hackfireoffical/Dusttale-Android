# Android compatibility audit — 18 November 2026

## Upstream baseline

- Base project: TheoDeveloping/Dusttale-Android-Port.
- Android orientation is landscape and fullscreen in Project.xml.
- Android touch controls are under source/android/.
- The inspected upstream checkout contains the game's asset bundle; this repository does not redistribute it.
- All 36 chart JSON files parsed successfully.
- The engine contains Dust-specific note rendering and chart effects.

## Limited compatibility work

- Added a Haxe-native implementation of selected receptor-motion sequences.
- Added a script to apply those changes to a local upstream checkout.
- This is not a complete Android port and does not establish full gameplay or visual parity.

## Build status

- No APK was produced.
- The automated APK workflow was removed.
- This repository is limited to non-weapon rhythm-game compatibility research; it does not package the complete game.
