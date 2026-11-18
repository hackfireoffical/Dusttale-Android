# Dusttale Android

An Android porting project for the existing Dusttale Remastered Android game.

## Goal

Build an installable Android version that preserves the game's original rhythm gameplay, songs, charts, note types, character animations, cutscenes, and visual effects while improving compatibility with modern Android devices.

## Upstream project

The game engine and original game assets are maintained in [TheoDeveloping/Dusttale-Android-Port](https://github.com/TheoDeveloping/Dusttale-Android-Port). This repository keeps the Android compatibility patch and build automation separate; it does not mirror the upstream asset bundle.

## Android compatibility work

- Validated all 36 chart JSON files in the inspected upstream checkout.
- The upstream engine already contains Dust-specific note rendering, gameplay effects, and Android touch controls.
- Added native Haxe support for receptor-motion sequences used by Hallucinations, Reality Check, and Last Hope. Arbitrary Lua modcharts are not enabled on Android; these three built-in sequences are ported natively.
- A GitHub Actions workflow checks out the upstream game, applies the patch, and attempts an Android APK build.

## Build status

The first automated build is being validated. An APK will only be announced as ready after the build succeeds and the generated package is checked.

## Credits and rights

Dusttale and Friday Night Funkin' are fan works based on their respective creators' intellectual property. Original game assets remain in the upstream project and are not redistributed here. Please follow the upstream project's license and the asset creators' terms.
