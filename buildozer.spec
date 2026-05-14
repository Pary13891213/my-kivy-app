[app]
title = تست سلام
package.name = salamtest
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt,json

requirements = python3==3.10.14, kivy==2.3.0, arabic_reshaper, python-bidi

version = 0.1
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# مهم برای رفع خطاهای قدیمی
android.skip_update = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
