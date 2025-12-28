# 01FletTextEditor app

![img](/home/mhcrnl/Desktop/Decembrie_2025/Markdown-editor-Flet/01_flet_text_editor/img/01_img.png)

Hai să construim un **editor de text în Flet**, cu **stocare persistentă locală**, simplu și funcțional.  
Îți ofer un exemplu complet, pe care îl poți rula imediat.

---

# 📝 Editor de text în Flet cu stocare persistentă (fișier local)

Vom folosi:

- **Flet** pentru UI
- **Un fișier `.txt`** pentru salvarea automată a textului

---

# 📁 Structura proiectului

```
text_editor/
 ├── main.py
 └── document.txt   (se creează automat)
```

---

# 🧠 Cod complet — `main.py`

```python
import flet as ft
import os

FILE_PATH = "document.txt"


def load_text():
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main(page: ft.Page):
    page.title = "Editor de text - Flet"
    page.window_width = 600
    page.window_height = 700

    text_content = load_text()

    editor = ft.TextField(
        value=text_content,
        multiline=True,
        min_lines=30,
        max_lines=None,
        expand=True,
        on_change=lambda e: save_text(editor.value),
        border_radius=10,
        border_color="blue",
        cursor_color="blue",
    )

    save_button = ft.ElevatedButton(
        "Salvează manual",
        icon=ft.icons.SAVE,
        on_click=lambda e: save_text(editor.value),
    )

    page.add(
        ft.Text("Editor de text cu stocare persistentă", size=20, weight="bold"),
        editor,
        save_button
    )


ft.app(target=main)
```

---

# ✔ Ce poate acest editor

### ✏ Editare text în timp real

Scrii direct în câmpul mare de text.

### 💾 Salvare automată

De fiecare dată când tastezi, conținutul este salvat în `document.txt`.

### 💾 Salvare manuală

Butonul „Salvează manual” este util dacă vrei control suplimentar.

### 🔄 Persistență

La redeschiderea aplicației, textul este încărcat automat.

---

# 🔧 Vrei versiunea cu:

- **formatări (bold, italic, underline)**
- **toolbar cu butoane**
- **salvare în Firebase**
- **export PDF**
- **multi-documente (tab-uri)**

Spune-mi ce variantă vrei să o construim mai departe.

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://docs.flet.dev/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://docs.flet.dev/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://docs.flet.dev/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://docs.flet.dev/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://docs.flet.dev/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://docs.flet.dev/publish/windows/).