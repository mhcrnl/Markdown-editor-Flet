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

ft.run(main)
