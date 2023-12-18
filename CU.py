import flet as ft
from time import sleep
#Esta de acá es para saber si es empleado o es Usuario normal
class CU(ft.UserControl):
    #Constructor
    def __init__(self, Page)-> None:
        super().__init__()
        self.Page=Page
        self.texto =  self.text1= ft.Text( "¿Qué tipo de usuario eres?",style=ft.TextThemeStyle.DISPLAY_LARGE, color = ft.colors.BLACK, font_family="Medium 500 Italic",opacity=1, animate_opacity=300,  left = 170, top = 100)
        self.btn1=ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Trabajador", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
            ), height= 100, width= 300, top= 400, left= 150, style=(ft.ButtonStyle( shape=(ft.RoundedRectangleBorder(radius=10)) ))
        )
        self.btn2=ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Cliente", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
            ), height= 100, width= 300, top= 400, right= 150, style=(ft.ButtonStyle( shape=(ft.RoundedRectangleBorder(radius=10)) ))
        )
        self.stak1 = ft.Stack([ self.btn1, self.btn2, self.text1],width=1080, height = 820, opacity=0, animate_opacity=1000)
    def met(self, met):
        self.btn1.on_click=met
    def animate(self):
        for x in range(1, 10, 1):
            self.stak1.opacity+=0.1
            self.stak1.update()
            sleep(0.1)
    #Es lo que regresa esta clase para ser un componente visual
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.WHITE,
    )