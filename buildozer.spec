[app]
title =KOS_VPN
package.name = KOS_VPN
package.domain = t.me/kos_VPN132
source.dir = .
version = 1.0
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow
orientation = portrait
icon.filename = %(source.dir)s/logo.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
fullscreen = 0
android.api = 31
android.minapi = 21
android.permissions = INTERNET
