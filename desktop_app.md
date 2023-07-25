# デスクトップアプリのパッケージ化

## pyinstallerのインストール

```sh:
>pip install pyinstaller
Collecting pyinstaller
  Obtaining dependency information for pyinstaller from https://files.pythonhosted.org/packages/cb/80/518fd6576f60aae9cc1cc96f133671d229cd85cd6dc14e7992dd2b5c498a/pyinstaller-5.13.0-py3-none-win_amd64.whl.metadata
  Downloading pyinstaller-5.13.0-py3-none-win_amd64.whl.metadata (8.3 kB)
:
Installing collected packages: altgraph, pywin32-ctypes, pyinstaller-hooks-contrib, pefile, pyinstaller
Successfully installed altgraph-0.17.3 pefile-2023.2.7 pyinstaller-5.13.0 pyinstaller-hooks-contrib-2023.6 pywin32-ctypes-0.2.2
```

## アプリのビルド

```sh:
>flet pack helloworld.py
Updating Flet View version info C:\Users\xxxx\AppData\Local\Temp\2f7bb157-91ba-4634-b275-5fcbcd856b91\flet\flet.exe
Running PyInstaller: ['helloworld.py', '--noconsole', '--noconfirm', '--onefile', '--version-file', 'C:\\Users\\xxxx\\AppData\\Local\\Temp\\5ebb35e6-1c25-470b-b986-a2d8f75a2830']
:
26060 INFO: Building EXE from EXE-00.toc completed successfully.
Deleting temp directory: C:\Users\xxxx\AppData\Local\Temp\2f7bb157-91ba-4634-b275-5fcbcd856b91
```

### distフォルダにアプリの実行ファイルが生成される

- build\helloworld
- dist
  - helloworld.exe

### アプリの名前、アイコンの指定

- アイコンの指定には、Pillow モジュールが必要

```sh:
>pip install pillow
Collecting pillow
  Obtaining dependency information for pillow from https://files.pythonhosted.org/packages/66/d4/054e491f0880bf0119ee79cdc03264e01d5732e06c454da8c69b83a7c8f2/Pillow-10.0.0-cp311-cp311-win_amd64.whl.metadata
  Downloading Pillow-10.0.0-cp311-cp311-win_amd64.whl.metadata (9.6 kB)
Downloading Pillow-10.0.0-cp311-cp311-win_amd64.whl (2.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 16.0 MB/s eta 0:00:00        
Installing collected packages: pillow
Successfully installed pillow-10.0.0
```

```sh:
>flet pack helloworld.py --name greet --icon img/helloworld.png
```