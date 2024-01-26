---
title: Test
---

```shell
pyinstaller --noconfirm --onefile -n "app_macos" --windowed --add-data "/Users/kittipos/my_app/simple-ctk-test/.venv/lib/python3.11/site-packages/customtkinter:customtkinter" app.py
```

```shell
pyinstaller --noconfirm --onefile -n "app_macos" --windowed --add-data "./.venv/lib/python3.11/site-packages/customtkinter:customtkinter" app.py
```

## Mac

### No add data 

Not work in local

```shell
pyinstaller --noconfirm --onefile -n "my-app" --windowed --icon="assets/icon.ico" app.py
```

### Add data

Work in local

```shell
pyinstaller --noconfirm --onefile -n "my-app" --windowed --add-data "./.venv/lib/python3.11/site-packages/customtkinter:customtkinter" --icon="assets/icon.ico" app.py
```

To convert `.app` to `.tar.gz`

```shell
tar -czf my-app.tar.gz my-app.app
```

## Windows

