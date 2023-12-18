import flet as ft
import pymysql
class solicitudes(ft.UserControl):
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
                ft.WindowDragArea(ft.Container(ft.Text("Estas son las solicitudes que te han enviado."), bgcolor=ft.colors.GREEN_300, padding=10), expand=True)
            ]
        )
        self.princ = ft.Column(scroll=ft.ScrollMode.AUTO, width=1080, height=2000, top=80, left=0)
        self.stak1 = ft.Stack([self.barra, self.princ],width=1080, height = 820)
    def lista(self):
        top=50
        cont = 1
        h = 820
        l = 0
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        print(self.yo)
        try:
                with conn.cursor() as cursor:
                        cursor.execute("SELECT ID, Usuario_Recibe, Usuario_Envia, estado, trabajo from `art`.`solicitud` where Usuario_Envia=%s ", self.yo)
                        resultado =cursor.fetchall()
                        for ID, usuarioR, UsuarioE, estado, trabajo in resultado:
                            fotos = ("Usuario/fotos/foto"+ str(l)+".jpg")
                            l+=1
                            if(estado=='Enviado'):
                                print("Sí entró")
                                cursor.execute("SELECT Imagen, Precio from `art`.`trabajador` where Usuario=%s ", usuarioR)
                                e =cursor.fetchone()    
                                img = e[0]
                                with open(fotos, 'wb') as q:
                                    q.write(img)
                                avatar =ft.Row([ft.CircleAvatar(
                                content=ft.Image(
                                    src=fotos, 
                                    fit=ft.ImageFit.COVER, border_radius=70, width=100
                                ), radius=50
                            )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                name = ft.Text(value=("Usuario: "), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Solicitud enviada, en espera de respuesta."),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+usuarioR), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.ORANGE_100)
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
                                top+=50   
                                cont+=1
                            if(estado=='Aceptado'):
                                cursor.execute("SELECT Imagen, Precio from `art`.`trabajador` where Usuario=%s ", usuarioR)
                                e =cursor.fetchone()    
                                img = e[0]
                                with open(fotos, 'wb') as q:
                                    q.write(img)
                                avatar =ft.Row([ft.CircleAvatar(
                                content=ft.Image(
                                    src=fotos, 
                                    fit=ft.ImageFit.COVER, border_radius=70, width=100
                                ), radius=50
                            )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                name = ft.Text(value=("Usuario: "), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Solicitud aceptada, en espera de que realice el servicio."),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+usuarioR), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.YELLOW_ACCENT_100
                                )
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
                                top+=50   
                                cont+=1
                            if(estado=='Rechazada' or estado=='Borrada'):
                                cursor.execute("SELECT Imagen, Precio from `art`.`trabajador` where Usuario=%s ", usuarioR)
                                e =cursor.fetchone()    
                                img = e[0]
                                with open(fotos, 'wb') as q:
                                    q.write(img)
                                avatar =ft.Row([ft.CircleAvatar(
                                content=ft.Image(
                                    src=fotos, 
                                    fit=ft.ImageFit.COVER, border_radius=70, width=100
                                ), radius=50
                            )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                name = ft.Text(value=("Rechazada."), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Solicitud rechazada."),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+usuarioR), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Borrar", icon=ft.icons.SEND, bgcolor="RED", width=150, height=40, on_click= lambda evento, c = ID: self.borrarsol(c))
                                soli.controls.append(but1)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.RED)
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
                                top+=50   
                                cont+=1
                            if(estado=='Terminado'):
                                cursor.execute("SELECT Imagen, Precio from `art`.`trabajador` where Usuario=%s ", usuarioR)
                                e =cursor.fetchone()    
                                img = e[0]
                                with open(fotos, 'wb') as q:
                                    q.write(img)
                                avatar =ft.Row([ft.CircleAvatar(
                                content=ft.Image(
                                    src=fotos, 
                                    fit=ft.ImageFit.COVER, border_radius=70, width=100
                                ), radius=50
                            )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                name = ft.Text(value=("Terminado."), size=25, color= ft.colors.BLACK)
                                drop = ft.Dropdown(label="Calificación",
                                             hint_text="Califica el servicio.",
                                            width=300,  bgcolor=ft.colors.GREEN_200, focused_bgcolor= ft.colors.GREEN_200,
                                            options=[
                                                ft.dropdown.Option("1"),
                                                ft.dropdown.Option("2"),
                                                ft.dropdown.Option("3"),
                                                ft.dropdown.Option("4"),
                                                ft.dropdown.Option("5"),
                                            ])
                                row2 = ft.Row([drop])
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Pagar", icon=ft.icons.SEND, bgcolor="GREEN", width=150, height=40, on_click= lambda evento, d = drop, pago =e[1],c = ID: self.pagarsol(c, pago, d.value))
                                soli.controls.append(but1)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.GREEN_100)
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
                                top+=50   
                                cont+=1
                            if(estado=='Pagado'):
                                cursor.execute("SELECT Imagen, Precio from `art`.`trabajador` where Usuario=%s ", usuarioR)
                                e =cursor.fetchone()    
                                img = e[0]
                                with open(fotos, 'wb') as q:
                                    q.write(img)
                                avatar =ft.Row([ft.CircleAvatar(
                                content=ft.Image(
                                    src=fotos, 
                                    fit=ft.ImageFit.COVER, border_radius=70, width=100
                                ), radius=50
                            )], alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                name = ft.Text(value=("Pagada y completada."), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Solicitud completada y pagada."),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+usuarioR), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Borrar", icon=ft.icons.SEND, bgcolor="RED", width=150, height=40, on_click= lambda evento, c = ID: self.borrarcom(c))
                                soli.controls.append(but1)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.LIGHT_GREEN_ACCENT_700)
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
                                top+=50   
                                cont+=1
        finally:

                # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
                conn.close()
    def show_drawer(self, e):
        self.Page.drawer.open = True
        self.Page.drawer.update()
    def rechazarsol(self, ID):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE `art`.`solicitud` SET `estado` = 'Rechazada' WHERE (`ID` = %s);"
                cursor.execute(sql, ID)
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def borrarsol(self, ID):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "DELETE FROM `art`.`solicitud` WHERE (`ID` = %s);"
                cursor.execute(sql, ID)
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def pagarsol(self, ID, precio, cal):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql2 = "INSERT INTO `art`.`pagos` (`solicitud_ID`, `pago`, `Puntuacion`) VALUES (%s, %s, %s);"
                sql = "UPDATE `art`.`solicitud` SET `estado` = 'Pagado' WHERE (`ID` = %s);"
                val2 = (ID, precio, cal)
                cursor.execute(sql2, val2)
                cursor.execute(sql, ID)
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def borrarcom(self, ID):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE `art`.`solicitud` SET `estado` = 'Historial' WHERE (`ID` = %s);"
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