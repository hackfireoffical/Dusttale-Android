# Dusttale Android

Android port work for **Friday Night Funkin': Dusttale Remastered**.

## Goal

Produce an installable Android build while preserving the original 2D rhythm-game experience: songs, charts, custom notes, character animations, cutscenes, visual effects, and touchscreen controls.

## Current technical base

The build uses the existing Android-focused engine project [TheoDeveloping/Dusttale-Android-Port](https://github.com/TheoDeveloping/Dusttale-Android-Port). This repository contains Android compatibility patches and a GitHub Actions workflow that builds the upstream source with those patches applied.

The patch adds native receptor-motion handling for selected chart sequences. It is not a general Lua modchart runtime, so exact timing and visual parity still require testing.

## Build status

GitHub Actions is being used to validate the Android toolchain and produce an APK artifact. A build is not considered complete until the APK has been generated successfully and tested on an Android device.

## Version / assets note

The upstream Android project supplies the current game assets. The GameBanana 1.1 download archive has not yet been verified as merged into this build, so this repository must not be described as a confirmed port of that exact archive.

## Credits and rights

Dusttale and Friday Night Funkin' are fan works. Original code and assets remain with their respective creators and upstream project. Follow the upstream license and the asset creators' terms.
