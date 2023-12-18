import flet as ft
import sqlite3
class listUU(ft.UserControl):
    def __init__(self, Page)-> None:
        super().__init__()
        self.Page=Page
        self.amenity_chips = []
        self.opciones = ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color="blue400",
                    icon_size=50,
                    tooltip="Menú", on_click= self.show_drawer
                )
        self.barra = ft.Row(
            [   self.opciones,
                ft.WindowDragArea(ft.Container(ft.Text("Bienvenido"), bgcolor=ft.colors.GREEN_300, padding=10), expand=True)
            ]
        )
        self.row9 =ft.Column([ft.Row([ft.Text("¿Qué servicios buscas?", size=25, color= ft.colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 40), ft.Row(self.amenity_chips, alignment=ft.MainAxisAlignment.CENTER, width= 1080, height= 60, wrap=True)], alignment=ft.MainAxisAlignment.CENTER, animate_opacity=300)
        self.stak1 = ft.Stack([self.barra,  self.row9],width=1080, height = 820)
    def lista(self, met):
        cont = 0
        amenities = ["Niñero", "Plomero", "Paseador de perros", "Albañil", "Fontanero", "Chofer", "Repartidor", "Reparador", "Jardinero"]
        for amenity in amenities:
            conn = sqlite3.connect("mibase.db")
            try:
                    cursor = conn.cursor()
                    conn.commit()
                    usere = (("%"+amenity+"%"),)
                    cursor.execute("SELECT User FROM anuncio AS p WHERE Profesion LIKE ?;", usere)
                    resultado =cursor.fetchone()
                    if resultado:
                        self.amenity_chips.append(
                         ft.TextButton(amenity, icon="chair_outlined", on_click=lambda evento, c=cont:met(amenities[c]))
                        )  
                    cont += 1
                    
                    
            finally:

                # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
                self.stak1.update()
                conn.close()
    def show_drawer(self, e):
        self.Page.drawer.open = True
        self.Page.drawer.update()      
    def build(self):
        return ft.Container(
        ft.Column([self.stak1], width= self.Page.window_width, scroll= "Auto"),
        alignment=ft.alignment.center,
        width=self.Page.window_width,
        height=self.Page.window_height,
        bgcolor=ft.colors.WHITE,
    )