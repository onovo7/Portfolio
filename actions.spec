# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Dell\\Desktop\\Python\\Baigiamasis_darbas\\Email_Checker\\actions.py'],
    pathex=[],
    binaries=[],
    datas=[('Baigiamasis_darbas\\\\Email_Checker\\\\dist\\\\Email_Checker.ui', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='actions',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
