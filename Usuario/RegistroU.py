import flet as ft
from time import sleep
from Usuario.CUsuario import *
class RegistroU(ft.UserControl):
    def __init__(self, Page)-> None:
        super().__init__()
        self.Page=Page
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.pick_files_dialog2 = ft.FilePicker(on_result=self.pick_files_result2)
        self.selected_files = ft.Text( size=15, color= ft.colors.BLACK)
        self.selected_file = ft.Text( size=15, color= ft.colors.BLACK)
        self.foto = ""
        self.document = ""
        self.user = ft.TextField(label="Usuario", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True)
        self.pas = ft.TextField(label="Contraseña", prefix_icon=ft.icons.SECURITY,  width= 400, border_color="white", password=True, can_reveal_password=True, color="black", filled= True)
        self.nombre= ft.TextField(label="Nombre", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True)
        self.ap = ft.TextField(label="Apellido", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True)
        self.fe = ft.TextField(label="Fecha", width= 100, border_color="white", color="black", filled= True)
        self.cvv = ft.TextField(label="CVV",  width= 100, border_color="white", color="black", filled= True,  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), max_length=3)
        self.tel = ft.TextField(label="Telefono", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True)
        self.direccion = ft.TextField(label="Diección", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True)
        self.tarj = ft.TextField(label="# de tarjeta", prefix_icon=ft.icons.EMOJI_EMOTIONS, width= 400, border_color="white", color="black", filled= True,  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""))
        self.button=  ft.IconButton(content= ft.Image(
        src="multimedia\Imagenes\Close_6.png", height=50, width=50
    ),
                    icon_color="red",
                    tooltip="Cerrar",
                top= 0, right=0, on_click= lambda _: self.Page.window_close())
        self.buttonb=  ft.IconButton(content= ft.Image(
        src="multimedia\Imagenes\Back Arrow_6.png",height=50, width=50
    ),
                    icon_color="red",
                    tooltip="Cerrar",
                top= 0, left=0, on_click= lambda _: self.Page.window_close())
        self.Page.overlay.append(self.pick_files_dialog)

        self.Page.overlay.append(self.pick_files_dialog2)

        self.text1= ft.Text( style=ft.TextThemeStyle.DISPLAY_LARGE, color = ft.colors.WHITE, font_family="Medium 500 Italic",opacity=0, animate_opacity=300,  left = 300, top = 30)
        
        self.row1 =ft.Column([ft.Row([ft.Text("Ingresa un usuario", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.user], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=130, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row2 =ft.Column([ft.Row([ft.Text("Ingresa una contraseña", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.pas], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=280, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0 )

        self.row3 =ft.Column([ft.Row([ft.Text("Ingresa tu nombre", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.nombre], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=430, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row4 =ft.Column([ft.Row([ft.Text("Ingresa tu apellido", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.ap], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=580, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row5 =ft.Column([ft.Row([ft.Text("Ingresa tu método de pago", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.tarj, self.fe, self.cvv], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=730, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row6 =ft.Column([ft.Row([ft.Text("Ingresa tu número de telefono", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.tel], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=880, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row7 =ft.Column([ft.Row([ft.Text("Ingresa tu dirección", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([self.direccion], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=1030, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)

        self.row8 =ft.Column([ft.Row([ft.Text("Ingresa un servicio publico.", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([ ft.ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: self.pick_files_dialog.pick_files(),
                    ),
                    self.selected_files,], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=1180, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)
        self.row9=ft.Column([ft.Row([ft.Text("Ingresa tu foto de perfil", size=25, color= ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row([ ft.ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: self.pick_files_dialog2.pick_files(),
                    ),
                    self.selected_file,], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=1330, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)
        self.row10 =ft.Column([ ft.Row([ft.FilledButton(
           "Enviar", width=150, col="black",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10), bgcolor= "white", color="black"
            ), on_click= lambda _: self.enviar(),
        )], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60)], top=1480, alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=0)    
        self.stak1 = ft.Stack([ft.Image(
        src="https://images.squarespace-cdn.com/content/v1/5b0b3909e7494053b798be8a/1543969371070-YEQMVBSRS6CLL7WH4OBQ/tumblr_omq8o7l1Hg1r4dhkuo1_r1_500.gif?format=1500w",
        width=1080,
        height=820*2,
        fit=ft.ImageFit.FILL,
        ),self.text1, self.button, self.buttonb, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8, self.row9,  self.row10],width=1080, height = 1600)
    def pick_files_result(self, e: ft.FilePickerResultEvent):
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        for x in e.files:
            self.foto = x.path
        self.selected_files.update()
    def enviar(self):
        usuario = self.user.value 
        nombre = self.nombre.value
        app = self.ap.value
        con= self.pas.value
        tell= self.tel.value
        foto= self.document
        recibo = self.foto
        tarjeta = self.tarj.value
        cvc = self.cvv.value
        fecha = self.fe.value
        dire = self.direccion.value
        T = cUsuario(usuario, nombre, app, dire, con, tarjeta, recibo, foto, tell, fecha, cvc)
        print(cvc)
        T.llenar()
        return T
    def pick_files_result2(self, e: ft.FilePickerResultEvent):
        self.selected_file.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        self.selected_file.update()
        for x in e.files:
            self.document=x.path
    def animateText(self):
        sleep(1)
        self.text1.opacity=1
        self.text1.value="BIENVENIDO"
        self.stak1.update()
        sleep(1)
        self.text1.opacity=0
        self.stak1.update()
        sleep(1)
        self.text1.value= "Por favor, ingresa tus datos."
        self.text1.left = 180
        self.text1.opacity=1
        self.stak1.update()
        sleep(0.5)
        self.row1.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row2.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row3.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row4.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row5.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row6.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row7.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row8.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row9.opacity=1
        self.stak1.update()
        sleep(0.3)
        self.row10.opacity=1
        self.stak1.update()
        
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.BLACK,
    )