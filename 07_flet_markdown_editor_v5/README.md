# 07FletMarkdownEditorV5 app

Perfect, hai să ducem editorul tău Markdown la nivelul următor și să adăugăm **export PDF real**.  
Vom folosi librăria **markdown** pentru conversia în HTML și **reportlab** pentru generarea PDF‑ului.

Este o soluție complet funcțională, 100% Python, fără servicii externe.

---

# 📦 Instalare librării necesare

Înainte de a rula aplicația, instalează:

```bash
pip install markdown reportlab
```

---

# 🧠 Cod complet — Editor Markdown + Toolbar + Dark Mode + Export PDF real

Acesta este codul complet, actualizat cu funcția reală de export PDF:

```python
import flet as ft
import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


FILE_PATH = "document.md"
PDF_OUTPUT = "document.pdf"


def load_text():
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def export_pdf_from_markdown(md_text):
    """Convertește Markdown în PDF real."""
    html = markdown.markdown(md_text)

    # Creăm PDF
    c = canvas.Canvas(PDF_OUTPUT, pagesize=letter)
    width, height = letter

    # Conversie simplă: eliminăm tag-urile HTML și păstrăm textul
    # (ReportLab nu randă HTML nativ)
    clean_text = html.replace("<p>", "").replace("</p>", "\n") \
                     .replace("<strong>", "").replace("</strong>", "") \
                     .replace("<em>", "").replace("</em>", "") \
                     .replace("<h1>", "").replace("</h1>", "") \
                     .replace("<h2>", "").replace("</h2>", "")

    text_object = c.beginText(1 * inch, height - 1 * inch)
    text_object.setFont("Helvetica", 12)

    for line in clean_text.split("\n"):
        text_object.textLine(line)

    c.drawText(text_object)
    c.save()


def main(page: ft.Page):
    page.title = "Editor Markdown complet"
    page.window_width = 1100
    page.window_height = 700

    page.theme_mode = ft.ThemeMode.LIGHT

    text_content = load_text()

    editor = ft.TextField(
        value=text_content,
        multiline=True,
        expand=True,
        min_lines=30,
        on_change=lambda e: update_preview(),
    )

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

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    def export_pdf(e):
        export_pdf_from_markdown(editor.value)
        page.snack_bar = ft.SnackBar(ft.Text("PDF generat: document.pdf"))
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
    # Panou dreapta
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

### 🖊 Toolbar complet
- Bold  
- Italic  
- Underline  
- H1  
- H2  
- Liste  

### 🌗 Dark Mode comutabil

### 📄 Export PDF real
- Convertește Markdown → HTML → text PDF  
- Generează fișierul `document.pdf` în folderul aplicației

### 📝 Editor Markdown complet
- Previzualizare live  
- Salvare automată  
- Layout profesional  

---

# Vrei să adaug și:
- suport pentru imagini în PDF  
- export PDF cu stiluri (bold, italic, titluri reale)  
- tab-uri pentru mai multe documente  
- autosave cu debounce  
- teme colorate (Dracula, Monokai, Solarized)

Spune-mi ce vrei să extindem.

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
