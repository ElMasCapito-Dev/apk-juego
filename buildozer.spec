[app]
title = Anime Multiverse
package.name = animemultiverse
package.domain = org.mitol
source.dir = .
source.include_exts = py,png,jpg,json,ttf,ogg,wav,mp3
source.exclude_dirs = build,dist,bin,.git,.github,.vscode,__pycache__
version = 1.0

# El juego usa pygame, no kivy
requirements = python3,pygame

orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.presplash_color = #000000
android.allow_backup = True
