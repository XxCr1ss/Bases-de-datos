import flet as ft
from Usuario.ISSU import *
class ISU(ft.UserControl):
    def __init__(self, Page)-> None:
        super().__init__()
        self.Page=Page
        self.texto =  self.text1= ft.Text( "Por favor, ingresa tus datos.",style=ft.TextThemeStyle.DISPLAY_LARGE, color = ft.colors.BLACK, font_family="Medium 500 Italic",opacity=1, animate_opacity=300,  left = 210, top = 30)
        self.user = ft.TextField(label="Username", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="white", filled= True)
        self.pas = ft.TextField(label="Contraseña", prefix_icon=ft.icons.SECURITY,
                                  width= 400, border_color="white", password=True, can_reveal_password=True, color="white", filled= True)
        self.btn1 = ft.FilledButton(
            "Iniciar sesión",width=200,height=200,
            style=ft.ButtonStyle(
                shape=ft.ContinuousRectangleBorder(radius=30),
            ), 
        )
        self.cont = ft.TextButton("¿No tienes una cuenta?", top= 490, right= 310)
        self.env = ft.Row([self.btn1],alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60, top =600)
        self.row1 =ft.Column([ft.Row([ft.Text("Ingresa tu usuario", size=25, color= ft.colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.user], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60),ft.Row([ft.Text("Ingresa tu contraseña", size=25, color= ft.colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60), ft.Row([self.pas], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=200, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=1, spacing=20 )
        self.stak1 = ft.Stack([ft.Image(
        src="https://i.pinimg.com/originals/f0/2c/40/f02c4046aa65d7a05cfb45720034b45c.gif",
        width=1080,
        height=820*2,
        fit=ft.ImageFit.FILL,
        ), self.row1, self.text1, self.env, self.cont],width=1080, height = 820,  animate_opacity=1000)
    def met(self, met):
        self.btn1.on_click=met
    def reg(self):
        self.cont.bgcolor="gray"
    def contra(self):
        return self.pas.value
    def use(self):
        return self.user.value
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.WHITE,
    )