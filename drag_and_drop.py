import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop"

    def drag_accept(e):
        print(vars(e))
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        if e.control.content.bgcolor == ft.colors.PINK_200:
            src.content.bgcolor = ft.colors.CYAN_200
            e.control.content.content.value = 0
            src.content.content.value = 1
        else:
            src.content.bgcolor = ft.colors.PINK_200
            e.control.content.content.value = 1
            src.content.content.value = 0
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                )
            ]
        )
    )
    print(vars(page))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
