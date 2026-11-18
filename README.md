# Dusttale Android

An independent Android-focused build project for the existing Dusttale Android port.

## Goal

Preserve the original Dusttale experience on Android: original story presentation, songs, chart timing, custom note types, gameplay effects, character animations, and touch controls. This is a compatibility/port project, not a remake or a replacement engine.

## Upstream

The source engine and game project are based on [TheoDeveloping/Dusttale-Android-Port](https://github.com/TheoDeveloping/Dusttale-Android-Port). The upstream repository contains the game assets; this repository does not redistribute those assets.

## Build

Open **Actions → Android APK Build → Run workflow**. The workflow checks out the upstream source and attempts an Android build. Successful runs publish an APK as a workflow artifact.

## Current engineering status

- 36 chart JSON files validated successfully in the inspected upstream checkout.
- The engine already contains Dust-specific note rendering and effects.
- Important Android compatibility work remains: song modcharts are gated to Windows in the current upstream code. Merely enabling that code on Android is not sufficient because its Lua runtime and bindings are Windows-only. These behaviors must be ported and tested individually before claiming feature parity.
- Android build has not yet been verified by this project.

## Credits and rights

Dusttale and Friday Night Funkin' are fan works built on their respective creators' intellectual property. This repository links to upstream source and does not include the original music, art, charts, or other game assets. Obtain and use those materials only in accordance with their creators' terms. Engine code remains subject to its upstream license.
