# 03FletMarkdownEditorV1 app

![](/home/mhcrnl/snap/marktext/9/.config/marktext/images/2025-12-28-09-59-12-image.png)

Hai să adăugăm **salvare în fișier** la editorul Markdown simplu din Flet.  
Îți ofer o versiune completă, curată și funcțională, care:

- încarcă textul dintr-un fișier la pornire
- salvează automat la fiecare modificare
- permite și salvare manuală printr-un buton

Este exact ce ai nevoie pentru un editor Markdown minimalist, dar util.

---

# 🧠 Cod complet — Editor Markdown + Salvare în fișier

```python
import flet as ft
import os

FILE_PATH = "document.md"


def load_text():
    """Încărcăm textul din fișier, dacă există."""
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    """Salvăm textul în fișier."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main(page: ft.Page):
    page.title = "Editor Markdown Simplu"
    page.window_width = 900
    page.window_height = 600

    # Text inițial încărcat din fișier
    text_content = load_text()

    # Editorul de text
    editor = ft.TextField(
        value=text_content,
        multiline=True,
        expand=True,
        min_lines=30,
        on_change=lambda e: update_preview(),  # salvare automată
    )

    # Previzualizare Markdown
    preview = ft.Markdown(
        value=text_content,
        expand=True,
        selectable=True,
    )

    # ---------------------------
    # Funcții
    # ---------------------------

    def update_preview():
        """Actualizează previzualizarea și salvează automat."""
        preview.value = editor.value
        save_text(editor.value)
        page.update()

    def save_manual(e):
        """Salvare manuală prin buton."""
        save_text(editor.value)
        page.snack_bar = ft.SnackBar(ft.Text("Salvat!"))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # UI Layout
    # ---------------------------

    save_button = ft.ElevatedButton(
        "Salvează",
        icon=ft.icons.SAVE,
        on_click=save_manual,
    )

    page.add(
        ft.Row(
            [
                ft.Container(editor, expand=1, padding=10),
                ft.VerticalDivider(),
                ft.Container(preview, expand=1, padding=10),
            ],
            expand=True,
        ),
        save_button,
    )


ft.app(target=main)
```

---

# ✔ Ce obții acum

### 📝 Editor Markdown complet funcțional

Scrii în stânga, vezi rezultatul în dreapta.

### 💾 Salvare automată

De fiecare dată când tastezi, fișierul `document.md` este actualizat.

### 💾 Salvare manuală

Butonul „Salvează” confirmă salvarea cu un mesaj vizual.

### 🔄 Persistență

La redeschiderea aplicației, textul este încărcat automat.

---

Dacă vrei, pot să adaug:

- toolbar cu Bold / Italic / H1 / liste
- dark mode
- export PDF
- suport pentru imagini
- multi-documente (tab-uri)

Spune-mi în ce direcție vrei să mergem mai departe.

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