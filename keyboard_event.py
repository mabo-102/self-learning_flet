import flet as ft

def main(page: ft.Page):
    def on_keyboared(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Cntr: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboared
    page.add(
        ft.Text("Press any key with a combination of Ctrl, Alt, Shift and Meta keys...")
    )

ft.app(target=main)
