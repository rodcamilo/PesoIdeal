[app]
# (str) Title of your application
title = PesoIdeal

# (str) Package name
package.name = pesoideal

# (str) Package domain (needed for android/ios packaging)
package.domain = org.rodcamilo

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target OS version / Fullscreen flag
fullscreen = 0

# Ícone principal
icon.filename = %(source.dir)s/icon.png

# Compatibilidade e estabilidade do Android SDK/NDK/Build-Tools
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
p4a.branch = release-2024.01.21

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
