# 02FletMarkedownDitor app

Hai să construim un **editor Markdown simplu** în **Flet**, exact cât trebuie ca să fie util, curat și ușor de extins.  
Îți ofer un exemplu complet, minimalist și funcțional: un `TextField` pentru editare și un `Markdown` pentru previzualizare live.

![img](/home/mhcrnl/Desktop/Decembrie_2025/Markdown-editor-Flet/02_flet_markedown_ditor/img/02_img.png)

---

# 🧩 Editor Markdown simplu în Flet

## ✔ Funcționalități:

- scrii Markdown în partea stângă
- vezi rezultatul în timp real în partea dreaptă
- totul într‑un layout responsive

---

# 🧠 Cod complet (simplu și clar)

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Editor Markdown Simplu"
    page.window_width = 900
    page.window_height = 600

    # Text inițial
    initial_text = "# Editor Markdown\nScrie Markdown în stânga."

    # Editorul de text
    editor = ft.TextField(
        value=initial_text,
        multiline=True,
        expand=True,
        min_lines=30,
        on_change=lambda e: update_preview(),
    )

    # Previzualizare Markdown
    preview = ft.Markdown(
        value=initial_text,
        expand=True,
        selectable=True,
    )

    # Funcție pentru actualizarea previzualizării
    def update_preview():
        preview.value = editor.value
        page.update()

    # Layout: editor stânga, preview dreapta
    page.add(
        ft.Row(
            [
                ft.Container(editor, expand=1, padding=10),
                ft.VerticalDivider(),
                ft.Container(preview, expand=1, padding=10),
            ],
            expand=True,
        )
    )

ft.app(target=main)
```

---

# 🎉 Ce obții

- un editor Markdown complet funcțional
- previzualizare live
- cod scurt, clar și ușor de extins
- perfect pentru notițe, documentație, prototipuri

---

# Vrei să adaug și:

- toolbar (Bold, Italic, H1, listă etc.)
- salvare în fișier
- dark mode
- export PDF
- suport pentru imagini

Spune-mi ce direcție vrei să urmăm și îl transformăm într-un editor serios.

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