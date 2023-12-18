import flet as ft
import sqlite3
class solicitud(ft.UserControl):
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
        conn = sqlite3.connect("mibase.db")
        try:
                        cursor = conn.cursor()
                        cursor.execute("SELECT ID,  Usuario_Envia, estado, trabajo from solicitud where Usuario_Recibe=? ", (self.yo,))
                        print(self.yo)
                        resultado =cursor.fetchall()
                        for ID,  UsuarioE, estado, trabajo in resultado:
                            fotos = ("Trabajador/fotos/foto"+ str(l)+".jpg")
                            l+=1
                            if(estado=='Enviado'):
                                cursor.execute("SELECT Foto, Direccion from usuario where User=? ", (UsuarioE,))
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
                                name = ft.Text(value=("Pendiente"), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Dirección: "+ e[1]),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Aceptar", icon=ft.icons.SEND, bgcolor="GREEN", width=150, height=40, on_click= lambda evento, c = ID: self.aceptarsol(c))
                                but2 =  ft.ElevatedButton("Rechazar", icon=ft.icons.CANCEL, bgcolor="RED", width=150, height=40, on_click= lambda evento, c = ID: self.rechazarsol(c))
                                soli.controls.append(but1)
                                soli.controls.append(but2)
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
                                cursor.execute("SELECT Foto, Direccion from usuario where User=? ", (UsuarioE,))
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
                                name = ft.Text(value=("Aceptado."), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Dirección: "+ e[1]),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.ElevatedButton("Terminar", icon=ft.icons.SEND, bgcolor="GREEN", width=150, height=40, on_click= lambda evento, c = ID, col=soli: self.terminarsol(c))
                                soli.controls.append(but1)
                                precio = ft.Text( ("Servicio: "+ trabajo), size=20, color = ft.colors.BLACK)
                                columna = ft.Column([name, user], spacing=5, alignment=ft.MainAxisAlignment.CENTER, expand=1)
                                columna2 = ft.Column([precio, row2], spacing=10, alignment=ft.MainAxisAlignment.CENTER, expand=2)
                                Vdivider = ft.VerticalDivider()
                                R= ft.Container(ft.Row([avatar, Vdivider, columna,columna2, soli], width=1080, height=120, ), bgcolor=ft.colors.YELLOW_100)
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
                            if(estado=='Rechazada'):
                                cursor.execute("SELECT Foto, Direccion from usuario where User=? ", (UsuarioE,))
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
                                name = ft.Text(value=("Rechazada. "), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Dirección: "+ e[1]),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
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
                            if(estado=='Terminado'):
                                cursor.execute("SELECT Foto, Direccion from usuario where User=? ", (UsuarioE,))
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
                                name = ft.Text(value=("Terminado. "), size=25, color= ft.colors.BLACK)
                                p =ft.Text( value= ("Dirección: "+ e[1]),size=18, color = ft.colors.BLACK)
                                row2 = ft.Row([p])
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
                                divider = ft.Divider()
                                soli =  ft.Column( alignment=ft.MainAxisAlignment.CENTER , expand=1, spacing=20)
                                but1=ft.Text( value= ("Esperando pago..."),size=18, color = ft.colors.BLACK)
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
                                cursor.execute("SELECT Foto, Direccion from usuario where User=? ", (UsuarioE,))
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
                                user = ft.Text(value=("@"+UsuarioE), size=18, color= ft.colors.BLACK)
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
        self.Page.end_drawer.open = True
        self.Page.end_drawer.update()
    def aceptarsol(self, ID):
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE solicitud SET estado = 'Aceptado' WHERE ID = ?;"
                cursor.execute(sql, (ID,))
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def rechazarsol(self, ID):
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE solicitud SET estado = 'Rechazada' WHERE ID = ?;"
                cursor.execute(sql, (ID,))
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def borrarsol(self, ID):
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE solicitud SET estado = 'Borrada' WHERE ID = ?;"
                cursor.execute(sql, (ID,))
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def terminarsol(self, ID):
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE solicitud SET estado = 'Terminado' WHERE ID = ?;"
                cursor.execute(sql, (ID,))
            # Confirmar la transacción
                conn.commit()
                self.princ.controls.clear()
                self.lista()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
    def borrarcom(self, ID):
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "UPDATE solicitud SET estado = 'Historial' WHERE ID = ?;"
                cursor.execute(sql, (ID,))
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