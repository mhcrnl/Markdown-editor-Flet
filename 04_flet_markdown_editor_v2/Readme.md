Sigur, hai să adăugăm **Dark Mode** elegant și simplu la editorul tău Markdown în Flet.  
Îți ofer o versiune completă în care utilizatorul poate comuta între **Light / Dark** cu un switch.

Totul rămâne minimalist, clar și ușor de extins.

![img](/home/mhcrnl/Desktop/Decembrie_2025/Markdown-editor-Flet/04_flet_markdown_editor_v2/img/04img.png)

---

# 🌙 Editor Markdown cu Dark Mode (comutabil)

### ✔ Include:

- Light / Dark Mode toggle
- Editor Markdown + Previzualizare
- Salvare automată în fișier
- UI adaptat la temă

---

# 🧠 Cod complet

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


ft.app(target=main)
```

---

# 🌗 Cum funcționează Dark Mode

- Comutatorul `Switch` schimbă `page.theme_mode` între:
  - `ft.ThemeMode.LIGHT`
  - `ft.ThemeMode.DARK`
- Flet aplică automat tema la toate componentele UI
- Markdown și TextField se adaptează automat

---

# Vrei să adaug și:

- **toolbar Markdown** (Bold, Italic, H1, liste)
- **dark mode automat după ora sistemului**
- **export PDF**
- **multi-documente (tab-uri)**

Spune-mi ce direcție vrei să urmăm.



import flet as ft

def main(page: ft.Page):

    def update_view(e):
        view.value = e.control.value
        view.update()
    
    page.padding=ft.padding.all(0)
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Editor Markdown"
    
    editor = ft.TextField(
        multiline=True,
        min_lines=20,
        max_lines=20,
        color='black',
        content_padding=30,
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.BLUE_GREY,
        on_change=update_view
    )
    
    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Divider(color='grey', height=40),
                ft.Text(value="Para criar Títulos", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="# H1", color='grey700'),
                ft.Text(value="## H2", color='grey700'),
                ft.Text(value="### H3", color='grey700'),
                ft.Text(value="...", color='grey700'),
                ft.Divider(color='grey', height=40),
    
                ft.Text(value="Para formatar textos", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="__texto em negrito__", color='grey700'),
                ft.Text(value="*texto itálico*", color='grey700'),
                ft.Text(value="*__texto em negrito e itálico__*", color='grey700'),
                ft.Text(value="~~texto tachado~~", color='grey700'),
                ft.Divider(color='grey', height=40),
    
                ft.Text(value="Para criação de listas", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value=" - Não ordenda", color='grey700'),
                ft.Text(value=" 1. Ordenada", color='grey700'),
                ft.Divider(color='grey', height=40),
    
                ft.Text(value="Para inserir links e imagens", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="[texto do link](url do link)", color='grey700'),
                ft.Text(value="![Texto da imagem](image.jpg)", color='grey700'),
                ft.Divider(color='grey', height=40),
    
                ft.Text(value="Para inserir código", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="`print(Código em uma linha)`", color='grey700'),
                ft.Text(value="```python\nprint('Código em múltiplas linhas')\n```", color='grey700'),
                ft.Divider(color='grey', height=40),
            ],
            spacing=10
        )
    )
    
    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link= lambda e: page.launch_url(e.data),
    )
    
    layout = ft.Row(
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to
                    ]
                )
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.Colors.BLACK,
                padding=ft.padding.all(30),
                content=view,
            ),
        ],
        spacing=0
    )
    
    page.add(layout)

if __name__=='__main__':
    ft.run(main)
