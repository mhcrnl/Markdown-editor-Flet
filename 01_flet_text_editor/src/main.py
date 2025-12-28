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
        icon=ft.Icons.SAVE,
        on_click=lambda e: save_text(editor.value),
    )

    page.add(
        ft.Text("Editor de text cu stocare persistentă", size=20, weight="bold"),
        editor,
        save_button
    )


ft.run(main)
