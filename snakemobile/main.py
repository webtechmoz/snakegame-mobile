from time import sleep
import asyncio
from controls.controls import (
    ft,
    randrange,
    Snake,
    Eat,
    Pontuation,
    Buttons
)

def main(page: ft.Page):
    page.title = 'Snake Game'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.all(2)
    page.appbar = ft.AppBar(bgcolor=ft.colors.GREY, toolbar_height=0)

    # Logica do jogo
    class Playing():
        def __init__(
            self,
        ):
            self.diretion = 'right'
        
        def keypressed(self, e: ft.ControlEvent | ft.KeyboardEvent):
            try:
                button: str = e.control.content.name

                if button == 'keyboard_arrow_up' and self.diretion in ['right', 'left']:
                    self.diretion = 'up'
                
                elif button == 'keyboard_arrow_down' and self.diretion in ['right', 'left']:
                    self.diretion = 'down'
                
                elif button == 'keyboard_arrow_left' and self.diretion in ['up', 'down']:
                    self.diretion = 'left'
                
                elif button == 'keyboard_arrow_right' and self.diretion in ['up', 'down']:
                    self.diretion = 'right'
            
            except:
                if e.key == 'Arrow Up' and self.diretion in ['right', 'left']:
                    self.diretion = 'up'
                
                elif e.key == 'Arrow Down' and self.diretion in ['right', 'left']:
                    self.diretion = 'down'
                
                elif e.key == 'Arrow Left' and self.diretion in ['up', 'down']:
                    self.diretion = 'left'
                
                elif e.key == 'Arrow Right' and self.diretion in ['up', 'down']:
                    self.diretion = 'right'
        
        def snake_eat(self, snake_head: Snake, eat: Eat):
            top = randrange(1, int(page.controls[0].controls[1].controls[0].height))
            left = randrange(1, int(page.width-10))
            
            if abs(snake_head.left - eat.left) < 12 and abs(snake_head.top - eat.top) < 12:
                eat.parent.controls.remove(eat)

                eat.parent.controls.append(
                    Eat(
                        left=left,
                        top=top,
                    )
                )

                snake_head.parent.controls.append(
                    Snake(
                        top=snake_head.parent.controls[-1].top,
                        left=snake_head.parent.controls[-1].left
                    )
                )

                points = eat.parent.parent.parent.parent.controls[0].controls[0].controls[-1]
                points.value = int(points.value) + 10

        async def snake_move(self):
            while True:
                try:
                    snake_body: list[Snake] = page.controls[0].controls[1].controls[0].content.controls[0].controls
                    snake_head: Snake = snake_body[0]
                    eat: Eat = page.controls[0].controls[1].controls[0].content.controls[1]

                    for i in range(len(snake_body)-1, 0, -1):
                        snake_body[i].left = snake_body[i-1].left
                        snake_body[i].top = snake_body[i-1].top

                    if self.diretion == 'right':
                        if snake_head.left < page.width - 10:
                            snake_head.left += 1
                        
                        else:
                            snake_head.left = 1
                    
                    elif self.diretion == 'left':
                        if snake_head.left > 0:
                            snake_head.left -= 1
                        
                        else:
                            snake_head.left = page.width - 10
                    
                    elif self.diretion == 'down':
                        if snake_head.top < snake_head.parent.parent.parent.height:
                            snake_head.top += 1
                        
                        else:
                            snake_head.top = 1
                    
                    elif self.diretion == 'up':
                        if snake_head.top > 0:
                            snake_head.top -= 1
                        
                        else:
                            snake_head.top = snake_head.parent.parent.parent.height

                    self.snake_eat(snake_head, eat)
                except Exception as e:
                    print(f'Erro: {e}')
                
                page.update()
                await asyncio.sleep(0.01)
    
    game = Playing()

    # Adicionando os controlos na página
    class Spacegame(ft.Column):
        def __init__(
            self
        ):
            super().__init__()
            self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            self.controls = [
                ft.Column(
                    controls=[
                        Pontuation(),
                        ft.Divider(
                            height=2,
                            thickness=1
                        )
                    ],
                    spacing=2
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={'xs': 12},
                            bgcolor=ft.colors.BLACK,
                            border_radius=1,
                            height=page.height * 0.60,
                            content=ft.Stack(
                                controls=[
                                    ft.Stack(
                                        controls=[
                                            Snake()
                                        ]
                                    ),
                                    Eat()
                                ]
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                Buttons(on_click=game.keypressed)
            ]

    page.add(Spacegame())
    page.on_keyboard_event = game.keypressed
    asyncio.run(game.snake_move())

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)