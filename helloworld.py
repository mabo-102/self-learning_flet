import flet as ft

def main(page: ft.Page):
    page.title = "Hello world"

    txt = ft.TextField(value="Hello Flet.")

    page.add(txt)

ft.app(target=main)