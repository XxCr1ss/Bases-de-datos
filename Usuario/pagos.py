import flet as ft
import pymysql
class pagos(ft.UserControl):
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
                ft.WindowDragArea(ft.Container(ft.Text("Estas son los pagos que has enviado."), bgcolor=ft.colors.GREEN_300, padding=10), expand=True)
            ]
        )
        self.princ = ft.Column(scroll=ft.ScrollMode.AUTO, width=1080, height=2000, top=80, left=0)
        self.stak1 = ft.Stack([self.barra, self.princ],width=1080, height = 820)
    def lista(self):
        cont = 1
        h = 820
        l = 0
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
                with conn.cursor() as cursor:
                        cursor.execute("SELECT ID,  Usuario_Recibe, estado from `art`.`solicitud` where Usuario_Envia=%s", self.yo)
                        resultado =cursor.fetchall()
                        for ID, UsuarioR, estado in resultado:
                            l+=1
                            if(estado=='Pagado' or estado=='Historial'):
                                cursor.execute("SELECT pago from `art`.`pagos` where solicitud_ID=%s ", ID)
                                e =cursor.fetchone()  
                                name = ft.Text(value=("Pagada y completada."), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Enviado: "+ str(e[0]) + "$"),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("Pagado a: @"+UsuarioR), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Borrar", icon=ft.icons.SEND, bgcolor="RED", width=150, height=40, on_click= lambda evento, c = ID: self.borrarcom(c))
                                soli.controls.append(but1)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([ Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.LIGHT_GREEN_ACCENT_700)
                                self.princ.controls.append(
                                R
                                )  
                                self.princ.controls.append(
                                divider
                                )
                                if(cont>=5):
                                    h+=150
                                    self.stak1.height=h
                                self.stak1.update() 
                                cont+=1
        finally:

                # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
                conn.close()
    def show_drawer(self, e):
        self.Page.end_drawer.open = True
        self.Page.end_drawer.update()
    def borrarcom(self, ID):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "DELETE FROM `art`.`pagos` WHERE (`ID` = %s);"
                cursor.execute(sql, ID)
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
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