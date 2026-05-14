[app]
title = برنامه من
package.name = myapp
package.domain = org.myapp

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt,json

requirements = python3==3.10.14, kivy==2.3.0, arabic_reshaper, python-bidi

version = 0.1
orientation = portrait
fullscreen = 0

# تنظیمات مهم Android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# این خط خیلی مهمه - اجازه نده خودش آپدیت کنه
android.skip_update = True
android.accept_sdk_license = True

android.permissions = INTERNET

[buildozer]
log_level = 2
