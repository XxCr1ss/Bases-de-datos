import flet as ft
import pymysql
class Anuncio(ft.UserControl):
    def __init__(self, Page, user)-> None:
        super().__init__()
        self.Page=Page
        self.yo = user
        self.opciones = ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color="blue400",
                    icon_size=50,
                    tooltip="Menú", on_click= self.show_drawer
                )
        self.barra = ft.Row(
            [   self.opciones,
                ft.WindowDragArea(ft.Container(ft.Text("Estos son los afiliados disponibles en su area para esta labor."), bgcolor=ft.colors.GREEN_300, padding=10), expand=True)
            ]
        )
        self.princ = ft.Column(scroll=ft.ScrollMode.AUTO, width=1080, height=820, top=80, left=0)
        self.stak1 = ft.Stack([self.barra, self.princ],width=1080, height = 820)
    def lista(self, profesion):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
                with conn.cursor() as cursor:
                    l = 0
                    conn.commit()
                    usere = ("%"+profesion+"%")
                    cursor.execute("SELECT User FROM anuncio WHERE Profesion LIKE %s;", usere)
                    resultado =cursor.fetchall()
                    for resultad in resultado:
                        fotos = ("Usuario/fotos/pfp"+ str(l)+".jpg")
                        l+=1
                        cursor.execute("SELECT Usuario, Nombre, Precio, Imagen from `art`.`trabajador` where Usuario=%s ", resultad)
                        r =cursor.fetchone()
                        use = ("@"+r[0])
                        nom = r[1]
                        prec= (str(r[2])+"/h")
                        img = r[3]
                        with open(fotos, 'wb') as q:
                           q.write(img)
                        avatar =ft.Row([ft.CircleAvatar(
                        content=ft.Image(
                            src=fotos, 
                            fit=ft.ImageFit.COVER, border_radius=70, width=100
                        ), radius=50
                    )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                        name = ft.Text(value=nom, size=45, color= ft.colors.BLACK)
                        star =ft.Icon(name=ft.icons.STAR, size=60, color=ft.colors.YELLOW_500)
                        p =ft.Text( "4.3",style=ft.TextThemeStyle.DISPLAY_MEDIUM, color = ft.colors.BLACK, font_family="Medium 500 Italic")
                        row2 = ft.Row([p, star])
                        user = ft.Text(value=use, size=22, color= ft.colors.BLACK)
                        divider = ft.Divider()
                        p = r[0]
                        soli =  ft.Column([ft.ElevatedButton("Solicitar.", icon=ft.icons.SEND, bgcolor="GREEN", width=150, height=60, on_click= lambda evento, c = p: self.enviarsol(c, profesion))], alignment=ft.MainAxisAlignment.CENTER , expand=1)
                        precio = ft.Text( prec,style=ft.TextThemeStyle.DISPLAY_MEDIUM, color = ft.colors.BLACK, font_family="Medium 500 Italic")
                        columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                        columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                        Vdivider = ft.VerticalDivider()
                        R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.BLUE_50)
                        self.princ.controls.append(
                         R
                        )  
                        self.princ.controls.append(
                         divider
                        )
                        self.stak1.update()
        finally:

                # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
                conn.close()
    def show_drawer(self, e):
        self.Page.drawer.open = True
        self.Page.drawer.update()
    def enviarsol(self, user2, trabajo):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "INSERT INTO `art`.`solicitud` (`Usuario_Recibe`, `Usuario_Envia`, `trabajo`) VALUES (%s, %s, %s);"
                print(self.yo)
                val = (user2, self.yo, trabajo)
                cursor.execute(sql, val)
            # Confirmar la transacción
                conn.commit()
               
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.WHITE,
    )