[app]

# (str) Title of your application
title = تست سلام

# (str) Package name
package.name = salamtest

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,kv,png,jpg,ttf,txt

# (list) Application requirements
# برای تست اولیه فقط kivy کافی است
requirements = python3,kivy

# (str) Application versioning (method 1)
version = 0.1

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API (30 پایدارتر است)
android.api = 30

# (int) Minimum API your APK will support
android.minapi = 21

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# ✅ این خط کلیدی برای رفع خطای PPA قدیمی است
android.skip_update = True

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

#
# Buildozer settings
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
