from time import sleep
import threading

import flet as ft


class Component1(ft.UserControl):
    def build(self):
        return ft.Text("APP")

class Component2(ft.UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = ft.Text(str(self.counter))
        return ft.Row([self.text, ft.ElevatedButton("Add", on_click=self.add_click)])

class Component3(ft.UserControl):
    def build(self):
        self.counter = 0
        text = ft.Text(str(self.counter))

        def add_click(e):
            self.counter += 1
            text.value = str(self.counter)
            self.update()

        return ft.Row([text, ft.ElevatedButton("Add", on_click=add_click)])


class Component4(ft.UserControl):
    def __init__(self, initial_count: int):
        super().__init__()
        self.counter = initial_count

    def build(self):
        text = ft.Text(str(self.counter))

        def add_click(e):
            self.counter += 1
            text.value = str(self.counter)
            self.update()

        return ft.Row([text, ft.ElevatedButton("Add", on_click=add_click)])


class Component5(ft.UserControl):
    def __init__(self, seconds: int):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.runnning = True
        self.th = threading.Thread(target=self.timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.runnning = False
        print("will_unmount.")

    def timer(self):
        while self.seconds and self.runnning:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = ft.Text()
        return self.countdown


def main(page):
    page.add(Component1())
    page.add(Component2())
    page.add(Component2())
    page.add(Component3())
    page.add(Component3())
    page.add(Component4(0))
    page.add(Component4(100))
    page.add(Component5(0))
    page.add(Component5(100))
    page.add(Component5(70))

if __name__ == "__main__":
    ft.app(main)
