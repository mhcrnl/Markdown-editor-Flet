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
    page.title = "Editor Markdown cu Bold"
    page.window_width = 900
    page.window_height = 600

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

    def insert_bold(e):
        # Inserează textul **bold**
        editor.value = (editor.value or "") + " **bold**"
        update_preview()

    # ---------------------------
    # Toolbar
    # ---------------------------

    toolbar = ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.FORMAT_BOLD,
                tooltip="Bold",
                on_click=insert_bold,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    # ---------------------------
    # Layout
    # ---------------------------

    page.add(
        toolbar,
        ft.Row(
            [
                ft.Container(editor, expand=1, padding=10),
                ft.VerticalDivider(),
                ft.Container(preview, expand=1, padding=10),
            ],
            expand=True,
        ),
    )


ft.run(main)
