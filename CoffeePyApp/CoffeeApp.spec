# -*- mode: python ; coding: utf-8 -*-

import sys

app_name = 'CoffeeApp'

block_cipher = None


a = Analysis(['CoffeePyApp.py'],
             pathex=['E:\\output\\app'],
             binaries=[],
             datas=[],
             hiddenimports=[
              'webbrowser',
			  '__init__',
			  'data.__init__',
			  'data.screens.__init__',
			  'data.screens.dbmanager',
			  'data.screens.db_kv.__init__',
			  'data.screens.db_kv.backupsd',
			  'scipy.special.cython_special',
             ],

             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
# exclusion list
from os.path import join
from fnmatch import fnmatch
exclusion_patterns = (
  join("kivy_install", "data", "images", "testpattern.png"),
  join("kivy_install", "data", "images", "image-loading.gif"),
  join("kivy_install", "data", "keyboards*"),
  join("kivy_install", "data", "settings_kivy.json"),
  join("kivy_install", "data", "logo*"),
  join("kivy_install", "data", "fonts", "DejaVuSans*"),
  join("kivy_install", "modules*"),
  join("Include*"),
  join("sdl2-config"),

  # Filter app directory
  join(".idea*"),
)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CoffeeApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='myicon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               Tree('C:\\Users\\izold\\AppData\\Local\\Programs\\Python\\Python37\\share\\sdl2\\bin\\'),
			   Tree('C:\\Users\\izold\\AppData\\Local\\Programs\\Python\\Python37\\share\\glew\\bin\\'),
               strip=False,
               upx=True,
               upx_exclude=[],
               name='CoffeeApp')
