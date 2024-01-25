---
title: Test
---

```shell
pyinstaller --noconfirm --onefile -n "app_macos" --windowed --add-data "/Users/kittipos/my_app/simple-ctk-test/.venv/lib/python3.11/site-packages/customtkinter:customtkinter" app.py
```

```shell
pyinstaller --noconfirm --onefile -n "app_macos" --windowed --add-data "./.venv/lib/python3.11/site-packages/customtkinter:customtkinter" app.py
```

```shell
pyinstaller --noconfirm --onefile -n "app" --windowed app.py
```

