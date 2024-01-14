import flet as ft

class SkeltonControl(ft.UserControl):
    def build(self):
      return ft.Text("Skelton!")

def main(page: ft.Page):
  page.add(SkeltonControl())

ft.app(target=main)
