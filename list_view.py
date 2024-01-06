from time import sleep

import flet as ft


def main(page: ft.Page):
    page.title = "Scroll Test"

    t = ft.Text("Scroll Test", color="Red", size=20)
    page.add(t)

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)

    for i in range(1,50):
        lv.controls.append(ft.Text(f"Line {i}"))
        if i > 25:
            sleep(1)
        page.update()

ft.app(target=main)
