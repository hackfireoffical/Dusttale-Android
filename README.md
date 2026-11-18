# Dusttale Android

An independent Android-focused build project for the existing Dusttale Android port.

## Goal

Explore safe Android compatibility work for the rhythm-game portions of the existing project, including chart timing, custom note rendering, and touch controls. This repository does not implement or package weapon-use gameplay.

## Upstream

The source engine and game project are based on [TheoDeveloping/Dusttale-Android-Port](https://github.com/TheoDeveloping/Dusttale-Android-Port). The upstream repository contains the game assets; this repository does not redistribute those assets.

## Current engineering status

- 36 chart JSON files validated successfully in the inspected upstream checkout.
- The engine already contains Dust-specific note rendering and effects.
- Added Android-native Haxe implementations for the three non-empty built-in receptor-motion modcharts (Hallucinations, Reality Check, Last Hope). The upstream Lua runtime remains Windows-only; arbitrary Lua modcharts are not enabled. The native port still needs in-game timing and visual verification.
- No APK build workflow is included. This repository currently contains the project audit and a limited Android-native chart-motion patch only.

## Credits and rights

Dusttale and Friday Night Funkin' are fan works built on their respective creators' intellectual property. This repository links to upstream source and does not include the original music, art, charts, or other game assets. Obtain and use those materials only in accordance with their creators' terms. Engine code remains subject to its upstream license.
