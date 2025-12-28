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
        icon=ft.Icons.SAVE,
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


ft.run(main)
