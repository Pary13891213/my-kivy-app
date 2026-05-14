[app]
title = تست سلام
package.name = salamtest
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt

requirements = python3,kivy

version = 0.1
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.skip_update = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
