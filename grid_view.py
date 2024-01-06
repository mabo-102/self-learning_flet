from time import sleep

import flet as ft


def main(page: ft.Page):
    page.title = "Scroll Test"

    t = ft.Text("Scroll Test", color="Red", size=20)
    page.add(t)

    gv = ft.GridView(expand=True, max_extent=100, child_aspect_ratio=1, auto_scroll=True)
    page.add(gv)

    for i in range(1,151):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Line {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.CYAN_300,
                border=ft.border.all(1, ft.colors.CYAN),
                border_radius=ft.border_radius.all(5)
            )
        )
        if i > 100:
            sleep(0.5)
        page.update()

ft.app(target=main)
