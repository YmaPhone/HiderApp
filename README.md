# Metrolist Image Hider for Windows

A Windows x64 installer that bundles patched Metrolist Desktop 14.0.0 (installer build 14.0.1) with a built-in image-visibility setting and a separate Hebrew-language quick switch.

## Included

- Metrolist Desktop for Windows x64, built from the upstream `v14.0.0` source and its submodules.
- A standalone **Metrolist Image Hider.exe**. Python does not need to be installed on the user's computer.
- Start Menu shortcuts for Metrolist and the image switch, plus optional Desktop shortcuts.

The switch writes `%APPDATA%\Metrolist\hide-images.flag`. The modified desktop app polls this setting, and a Coil image-loader interceptor blocks image requests while hiding is enabled. Dedicated player-background, lyrics-artwork, and artist-photo views also respect the setting.

## Build

GitHub Actions builds the installer on a Windows runner. It checks out the upstream Metrolist `v14.0.0` tag with submodules, applies `image-hider.patch`, builds the Windows desktop package and login helper, creates the standalone switch, and compiles an Inno Setup installer.

A successful run uploads the installer as a workflow artifact and attaches it to a GitHub Release. To build again, open **Actions → Build Windows Installer → Run workflow**.

## Notes

- This is a modified Metrolist build; installing the standalone switch alone will not change an existing Metrolist installation.
- The installer targets Windows x64.
- Optional Last.fm and Lyprio API credentials may be added as repository Actions secrets. Without them, those provider integrations may not be available in this build.
- Metrolist is licensed under GPL-3.0. See the [upstream license](https://github.com/MetrolistGroup/Metrolist/blob/v14.0.0/LICENSE). This repository contains the modification patch and packaging workflow, not ownership of the upstream project.
