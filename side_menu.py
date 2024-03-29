import flet as ft

def main(page: ft.Page):

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Checked item", checked=False,on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

    def side_menu():
        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            #extended=True,
            min_width=100,
            min_extended_width=300,
            leading=ft.FloatingActionButton(
                icon=ft.icons.CREATE_OUTLINED,
                text="New Manual"
            ),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER,
                    selected_icon=ft.icons.FAVORITE,
                    label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings")

                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index)
        )
        return rail

    def main_view():
        pass

    def thumbnail_view():
        pass

    page.add(
        ft.Row(
            [
                side_menu(),
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True)
            ],
            expand=True
        )
    )

ft.app(target=main)
