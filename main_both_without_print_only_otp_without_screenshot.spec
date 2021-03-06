# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

face_models = [
('.\\face_recognition_models\\models\\dlib_face_recognition_resnet_model_v1.dat', '.\\face_recognition_models\\models'),
('.\\face_recognition_models\\models\\mmod_human_face_detector.dat', '.\\face_recognition_models\\models'),
('.\\face_recognition_models\\models\\shape_predictor_5_face_landmarks.dat', '.\\face_recognition_models\\models'),
('.\\face_recognition_models\\models\\shape_predictor_68_face_landmarks.dat', '.\\face_recognition_models\\models'),
]

a = Analysis(['main_both_without_print_only_otp_without_screenshot.py'],
             pathex=['C:\\Users\\ABSTech\\Desktop\\Time_Tracker'],
             binaries=face_models,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Time Tracker',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\ABSTech\\Desktop\\Time_Tracker\\Airface1.ico' )
