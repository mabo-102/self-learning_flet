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

    def end_drawer_dismissed(e):
        print("End drawer dismissed!")

    end_drawer = ft.NavigationDrawer(
        on_dismiss=end_drawer_dismissed,
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.FAVORITE,
                label="First"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label="Settings"
            )
        ],
        on_change=lambda e: print(f"Selected destination:", e.control.selected_index)
    )

    def show_end_drawer(e):
        page.show_end_drawer(end_drawer)

    page.add(ft.ElevatedButton("Show end drawer", on_click=show_end_drawer))

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
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP,
                    label="Item 1"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.ADD_COMMENT,
                    label="Item 2"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.ADD_COMMENT,
                    label_content=ft.Text("Item 3")
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index)
        )
        return rail

    def main_view():
        pass

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index)
    )

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
