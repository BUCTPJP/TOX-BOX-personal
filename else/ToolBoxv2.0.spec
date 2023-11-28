# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ToolBoxv2.0.py'],
    pathex=['D:\\办公学习\\学习\\理\\编程设计\\python\\Python项目\\工具盒\\v2.0'],
    binaries=[],
    datas=[('img\\bg.jpg','img'),
           ('img\\bili_download.ico','img'),
           ('img\\common.ico','img'),
           ('img\\main.ico','img'),
           ('img\\math.ico','img'),
           ('img\\phy.ico','img'),
           ('img\\picture_torrent.ico','img'),
           ('img\\QRcode_anailzing.ico','img'),
           ('img\\QRcode_make.ico','img'),
           ('img\\word_frequency_en.ico','img'),
           ('使用说明\\词频统计(en)使用说明.txt','使用说明'),
           ('使用说明\\二维码生成使用说明.txt','使用说明'),
           ('使用说明\\图种制作使用说明.txt','使用说明'),
           ('使用说明\\B站视频下载器使用说明.txt','使用说明')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ToolBoxv2.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='img\\main.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ToolBoxv2.0',
)
