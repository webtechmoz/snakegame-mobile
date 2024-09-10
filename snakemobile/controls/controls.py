import flet as ft
from random import randrange

class Squad(ft.Container):
    def __init__(
        self,
        top: float = None,
        left: float = None,
        width: float = None,
        height: float = None,
        border_radius: float = None,
        bgcolor: ft.colors = None,
        content: ft.Control = None
    ):
        super().__init__()
        self.top = top
        self.height = left
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.bgcolor = bgcolor
        self.content = content

class Button(ft.Container):
    def __init__(
        self,
        on_click: ft.ControlEvent,
        icon: ft.icons = None,
        color: ft.colors = ft.colors.GREY,
        size: float = 20
    ):
        super().__init__()
        self.width = 40
        self.height = 40
        self.alignment = ft.alignment.center
        self.content = ft.Icon(
            name=icon,
            color=color,
            size=size
        )
        self.on_click = on_click

class Snake(Squad):
    def __init__(
        self,
        top: float = 12,
        left: float = 12
    ):
        super().__init__()
        self.width = 12
        self.height = 12
        self.top = top
        self.left = left
        self.bgcolor = ft.colors.WHITE

class Eat(Squad):
    def __init__(
        self,
        top: float = randrange(1, 384),
        left: float = randrange(1, 384),
        width: float = 15,
        bgcolor: ft.colors = ft.colors.BLUE
    ):
        super().__init__()
        self.top = top
        self.left = left
        self.width = width
        self.height = self.width
        self.border_radius = self.width
        self.bgcolor = bgcolor

class Pontuation(ft.Row):
    def __init__(
        self,
        value: int = 0
    ):
        self.color = ft.colors.GREEN
        super().__init__()
        self.alignment = ft.MainAxisAlignment.START
        self.spacing = 5
        self.controls = [
            ft.Icon(
                name=ft.icons.HOME_MAX,
                size=22,
                color=self.color
            ),
            ft.Text(
                value='Score:'.upper(),
                size=16,
                weight='bold',
                color=self.color
            ),
            ft.Text(
                value=value,
                size=16,
                weight='bold',
                color=self.color
            )
        ]

class Buttons(ft.Column):
    def __init__(
        self,
        on_click: ft.ControlEvent = None
    ):
        super().__init__()
        self.width = 150
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 0
        self.controls = [
            Button(icon=ft.icons.KEYBOARD_ARROW_UP, on_click=on_click),
            ft.Row(
                controls =[
                    Button(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=on_click),
                    Button(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=on_click)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=0
            ),
            Button(icon=ft.icons.KEYBOARD_ARROW_DOWN, on_click=on_click),
        ]