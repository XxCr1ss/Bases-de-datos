import flet as ft
import sqlite3
class domesticT(ft.UserControl):
    def __init__(self, Page)-> None:
        super().__init__()
        self.Page=Page
        self.opciones = ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color="blue400",
                    icon_size=50,
                    tooltip="Menú", on_click= self.show_drawer
                )
        self.img = ft.Image(
        src="https://i.pinimg.com/originals/7c/17/f0/7c17f0c64b977875a2c0625b406bb0d2.gif",
        width=1080,
        height=820,
        fit=ft.ImageFit.FILL,
        )
        self.pfp =  ft.CircleAvatar(
         radius=100)   
        self.name = ft.TextField(label="Nombre",  color = ft.colors.BLACK, text_size=45, read_only=True, border="underline")
        self.star =ft.Icon(name=ft.icons.STAR, size=60, color=ft.colors.YELLOW_500)
        self.add = ft.TextField(label="Precio", color = ft.colors.BLACK, text_size=20, read_only=True, border="underline")
        self.cel = ft.TextField(label="Celular",  color = ft.colors.BLACK, text_size=20, read_only=True, border="underline")
        self.user = ft.Text( "@PussyDestroyer", color = ft.colors.BLACK)
        self.c = ft.Column([self.name, self.user], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        self.p =ft.TextField( label = "Calificación.", value="4.3", color = ft.colors.BLACK, text_size=20, read_only=True, border="underline", suffix_icon=ft.icons.STAR, text_align=ft.TextAlign.CENTER)
        self.divider = ft.Divider(color=ft.colors.BLACK87)
        self.row1 =ft.Column([ft.Row([self.pfp], alignment=ft.MainAxisAlignment.CENTER), ft.Row([self.c], alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300, opacity=1)
        self.row2 = ft.Row([self.p], alignment=ft.MainAxisAlignment.CENTER, width= 1080)
        self.row3 = ft.Row([self.add], alignment=ft.MainAxisAlignment.CENTER, width= 1080)
        self.row4 = ft.Row([self.cel], alignment=ft.MainAxisAlignment.CENTER, width= 1080)
        self.colp = ft.Container(ft.Column([ self.row1, self.row2, self.row3, self.row4],scroll=ft.ScrollMode.AUTO, width=1080, height=820), bgcolor=ft.colors.WHITE30, top=80, left=0)
        self.barra = ft.Row(
            [   self.opciones,
            ],
            alignment= ft.MainAxisAlignment.END
        )
        self.stak1 = ft.Stack( [self.img, self.barra, self.colp],width=1080, height = 820,  animate_opacity=1000)
    def show_drawer(self, e):
        self.Page.end_drawer.open = True
        self.Page.end_drawer.update()
    def intcomp(self, user):
        conn = sqlite3.connect("mibase.db")
        try:
                    cursor = conn.cursor()
                    conn.commit()
                    usere = (user,)
                    fotos = ("Trabajador/fotos/pfp.jpg")
                    cursor.execute('''SELECT Usuario, Nombre, Apellido, Telefono, Imagen, Precio from trabajador where Usuario=?''', usere)
                    r =cursor.fetchone()
                    use = r[0]
                    nom = r[1]
                    Apellido=r[2]
                    cel = r[3]
                    img = r[4]
                    precio = r[5]
                    with open("Trabajador/fotos/pfp.jpg", 'wb') as q:
                        q.write(img)
                    self.name.value=(nom + " " + Apellido)
                    self.add.value=(str(precio)+"/h")
                    self.user.value= ("@"+use)
                    self.cel.value=cel
                    self.pfp.content=ft.Image(
                            src=fotos, 
                            fit=ft.ImageFit.FILL, border_radius=100, width=200, height=200
                        )
                    self.stak1.update()
        finally:

                # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
                self.stak1.update()
                conn.close()
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.WHITE,
    )