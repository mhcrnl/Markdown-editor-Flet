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
    page.title = "Editor Markdown cu Dark Mode"
    page.window_width = 900
    page.window_height = 600

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

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    # ---------------------------
    # UI
    # ---------------------------

    theme_switch = ft.Switch(
        label="Dark Mode",
        value=False,
        on_change=toggle_theme,
    )

    page.add(
        ft.Row(
            [
                theme_switch,
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
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
