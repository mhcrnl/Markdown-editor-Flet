# 06FletMarkdownEditorV4 app

Perfect, hai să construim un **editor Markdown complet**, cu:

### ✔ Toolbar:

- **Bold**

- *Italic*

- **Underline**

- # H1

- ## H2

- Liste (• bullet list)

### ✔ Panou dreapta:

- Dark Mode toggle
- Buton „Export PDF” (fără a genera PDF — doar butonul, pentru că Flet nu poate exporta PDF nativ)

### ✔ Funcționalități existente:

- Previzualizare Markdown live
- Salvare automată în fișier
- Layout editor + preview

Totul într-un singur cod, curat și ușor de extins.

---

# 🧠 Cod complet — Editor Markdown cu Toolbar + Dark Mode + Export PDF (UI)

```python
import flet as ft
import os

FILE_PATH = "document.md"


def load_text():
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main(page: ft.Page):
    page.title = "Editor Markdown complet"
    page.window_width = 1100
    page.window_height = 700

    # Tema implicită
    page.theme_mode = ft.ThemeMode.LIGHT

    # Text inițial
    text_content = load_text()

    # Editor text
    editor = ft.TextField(
        value=text_content,
        multiline=True,
        expand=True,
        min_lines=30,
        on_change=lambda e: update_preview(),
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
        preview.value = editor.value
        save_text(editor.value)
        page.update()

    def insert(text):
        editor.value = (editor.value or "") + text
        update_preview()

    # Toolbar actions
    def bold(e): insert(" **bold**")
    def italic(e): insert(" _italic_")
    def underline(e): insert(" __underline__")
    def h1(e): insert("\n# Titlu H1\n")
    def h2(e): insert("\n## Titlu H2\n")
    def bullet_list(e): insert("\n- element\n")

    # Dark mode toggle
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    # Export PDF (UI only)
    def export_pdf(e):
        page.snack_bar = ft.SnackBar(ft.Text("Export PDF nu este disponibil nativ în Flet."))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # Toolbar
    # ---------------------------

    toolbar = ft.Row(
        [
            ft.IconButton(icon=ft.icons.FORMAT_BOLD, tooltip="Bold", on_click=bold),
            ft.IconButton(icon=ft.icons.FORMAT_ITALIC, tooltip="Italic", on_click=italic),
            ft.IconButton(icon=ft.icons.FORMAT_UNDERLINED, tooltip="Underline", on_click=underline),
            ft.IconButton(icon=ft.icons.TITLE, tooltip="H1", on_click=h1),
            ft.IconButton(icon=ft.icons.SUBTITLES, tooltip="H2", on_click=h2),
            ft.IconButton(icon=ft.icons.LIST, tooltip="Listă", on_click=bullet_list),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    # ---------------------------
    # Panou dreapta: Dark mode + Export PDF
    # ---------------------------

    right_panel = ft.Column(
        [
            ft.Switch(label="Dark Mode", value=False, on_change=toggle_theme),
            ft.ElevatedButton("Export PDF", icon=ft.icons.PICTURE_AS_PDF, on_click=export_pdf),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
    )

    # ---------------------------
    # Layout final
    # ---------------------------

    page.add(
        toolbar,
        ft.Row(
            [
                ft.Container(editor, expand=2, padding=10),
                ft.VerticalDivider(),
                ft.Container(preview, expand=2, padding=10),
                ft.VerticalDivider(),
                ft.Container(right_panel, expand=1, padding=10),
            ],
            expand=True,
        ),
    )


ft.app(target=main)
```

---

# 🎉 Ce ai acum

### 🖊 Toolbar complet:

- **Bold**, *Italic*, **Underline**

- # H1, ## H2

- Liste cu bullet-uri

### 🌗 Dark Mode

Comutator în panoul din dreapta.

### 📄 Export PDF (UI)

Butonul există, iar tu poți ulterior integra o librărie externă pentru generarea PDF.

### 📝 Editor Markdown complet

- Previzualizare live
- Salvare automată
- Layout profesional

---

Dacă vrei, pot să adaug:

- **Export PDF real** (cu `reportlab` sau `markdown-pdf`)
- **Tab-uri pentru mai multe documente**
- **Toolbar extins (H3, citate, cod, imagini)**
- **Autosave cu debounce**
- **Teme personalizate (Monokai, Dracula, Solarized)**

Spune-mi ce vrei să îmbunătățim.

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