import flet as ft
import os
import shutil
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

FILE_PATH = "document.md"
PDF_OUTPUT = "document.pdf"
IMAGES_DIR = "images"

# ---------------------------
# Teme colorate
# ---------------------------
THEMES = {
    "Dracula": {
        "bg": "#282a36",
        "text": "#f8f8f2",
    },
    "Monokai": {
        "bg": "#272822",
        "text": "#f8f8f2",
    },
    "Solarized Dark": {
        "bg": "#002b36",
        "text": "#93a1a1",
    },
    "Solarized Light": {
        "bg": "#fdf6e3",
        "text": "#657b83",
    },
}


def load_text():
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def export_pdf_from_markdown(md_text):
    html = markdown.markdown(md_text)

    clean_text = (
        html.replace("<p>", "")
        .replace("</p>", "\n")
        .replace("<strong>", "")
        .replace("</strong>", "")
        .replace("<em>", "")
        .replace("</em>", "")
        .replace("<h1>", "")
        .replace("</h1>", "")
        .replace("<h2>", "")
        .replace("</h2>", "")
    )

    c = canvas.Canvas(PDF_OUTPUT, pagesize=letter)
    width, height = letter

    text_object = c.beginText(1 * inch, height - 1 * inch)
    text_object.setFont("Helvetica", 12)

    for line in clean_text.split("\n"):
        text_object.textLine(line)

    c.drawText(text_object)
    c.save()


def main(page: ft.Page):
    page.title = "Editor Markdown complet"
    page.window_width = 1200
    page.window_height = 750

    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    text_content = load_text()

    editor = ft.TextField(
        value=text_content,
        multiline=True,
        expand=True,
        min_lines=30,
    )

    preview = ft.Markdown(
        value=text_content,
        expand=True,
        selectable=True,
    )

    def update_preview():
        preview.value = editor.value
        save_text(editor.value)
        page.update()

    editor.on_change = lambda e: update_preview()

    def insert(text):
        editor.value = (editor.value or "") + text
        update_preview()

    def bold(e): insert(" **bold**")
    def italic(e): insert(" _italic_")
    def underline(e): insert(" __underline__")
    def h1(e): insert("\n# Titlu H1\n")
    def h2(e): insert("\n## Titlu H2\n")
    def bullet_list(e): insert("\n- element\n")

    def change_theme(e):
        theme_name = theme_dropdown.value
        theme = THEMES[theme_name]
        page.bgcolor = theme["bg"]
        editor.bgcolor = theme["bg"]
        editor.color = theme["text"]
        preview.bgcolor = theme["bg"]
        preview.code_theme = "atom-one-dark"
        page.update()

    def export_pdf(e):
        export_pdf_from_markdown(editor.value)
        page.snack_bar = ft.SnackBar(ft.Text("PDF generat: document.pdf"))
        page.snack_bar.open = True
        page.update()

    def pick_image(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        file = e.files[0]
        dest = os.path.join(IMAGES_DIR, file.name)
        shutil.copy(file.path, dest)
        insert(f"\n![imagine]({IMAGES_DIR}/{file.name})\n")

    file_picker = ft.FilePicker()
    file_picker.on_result = pick_image
    page.overlay.append(file_picker)

    toolbar = ft.Row(
        [
            ft.IconButton(icon=ft.icons.FORMAT_BOLD, tooltip="Bold", on_click=bold),
            ft.IconButton(icon=ft.icons.FORMAT_ITALIC, tooltip="Italic", on_click=italic),
            ft.IconButton(icon=ft.icons.FORMAT_UNDERLINED, tooltip="Underline", on_click=underline),
            ft.IconButton(icon=ft.icons.TITLE, tooltip="H1", on_click=h1),
            ft.IconButton(icon=ft.icons.SUBTITLES, tooltip="H2", on_click=h2),
            ft.IconButton(icon=ft.icons.LIST, tooltip="Listă", on_click=bullet_list),
            ft.IconButton(
                icon=ft.icons.IMAGE,
                tooltip="Adaugă imagine",
                on_click=lambda _: file_picker.pick_files(allow_multiple=False),
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    theme_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(t) for t in THEMES.keys()],
        value="Dracula",
        width=200,
    )
    theme_dropdown.on_change = change_theme

    right_panel = ft.Column(
        [
            ft.Text("Temă:", size=16, weight="bold"),
            theme_dropdown,
            ft.Divider(),
            ft.ElevatedButton("Export PDF", icon=ft.icons.PICTURE_AS_PDF, on_click=export_pdf),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
    )

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

    # aplică tema inițială
    change_theme(None)


ft.app(target=main)
