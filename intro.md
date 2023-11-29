# Flet入門

## Fletとは

- フロントエンド開発の経験がなくても、対話型のマルチユーザー Web、デスクトップ、モバイル アプリケーションを好みの言語で構築できるフレームワークです。

# 公式サイト

- [flet.dev](https://flet.dev/)

# インストール

```sh:
>pip install flet
Collecting flet
  Downloading flet-0.8.4-py3-none-win_amd64.whl (22.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.7/22.7 MB 34.4 MB/s eta 0:00:00    
:
Installing collected packages: wcwidth, pywin32, pypng, funcy, websockets, websocket-client, watchdog, typing-extensions, sniffio, six, pyyaml, pygments, prompt_toolkit, plumbum, pathspec, packaging, oauthlib, MarkupSafe, idna, h11, decorator, colorama, certifi, repath, questionary, qrcode, pyyaml-include, pydantic, jinja2, dunamai, anyio, jinja2-ansible-filters, httpcore, flet-core, httpx, copier, flet-runtime, flet
Successfully installed MarkupSafe-2.1.3 anyio-3.7.1 certifi-2023.7.22 colorama-0.4.6 copier-8.1.0 decorator-5.1.1 dunamai-1.18.0 flet-0.8.4 flet-core-0.8.4 flet-runtime-0.8.4 funcy-2.0 h11-0.14.0 httpcore-0.17.3 httpx-0.24.1 idna-3.4 jinja2-3.1.2 jinja2-ansible-filters-1.3.2 oauthlib-3.2.2 packaging-23.1 pathspec-0.11.1 plumbum-1.8.2 prompt_toolkit-3.0.39 pydantic-1.10.12 pygments-2.15.1 pypng-0.20220715.0 pywin32-306 pyyaml-6.0.1 pyyaml-include-1.3.1 qrcode-7.4.2 questionary-1.10.0 repath-0.9.0 six-1.16.0 sniffio-1.3.0 typing-extensions-4.7.1 watchdog-3.0.0 wcwidth-0.2.6 websocket-client-1.6.1 websockets-11.0.3
```

# Hot reload

```sh:
flet run todo.py
```