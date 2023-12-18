import flet as ft
from Trabajador.RegistroT import *
from CU import *
from Trabajador.IST import *
from Trabajador.ISST import *
from Usuario.ISU import *
from Usuario.ISSU import *
from Usuario.domesticU import *
from Usuario.list import *
from Trabajador.solicitud import *
from Trabajador.pagosT import *
from Usuario.pagos import *
from Usuario.solicitudes import *
from Usuario.anuncio import *
from Trabajador.ISST import *
from Trabajador.domesticT import *
from Usuario.RegistroU import *
#---------------------------Clase principal que maneja las demás ventanas----------------
#El usuario que está usando la app en ese momento
global UserU
#El trabajador que la está usando en ese momento
global userT
userT= ""
userU = ""
#Main
def main(page: ft.Page):
    init = 0
    page.window_height=820
    page.window_width=1080
    page.window_title_bar_hidden = False
    page.window_title_bar_buttons_hidden = True
    page.window_center()
#------------------Vistas------------------------
    I = ISU(page)
    d=IST(page)
    a = CU(page)
    buscarT = ISST
    buscarU = ISSU
    b = Registro(page)
    e = RegistroU(page)
    dT= domesticT(page)
    dU = domesticU(page)
    li = listUU(page)
    pa = pagos(page, userU)
    paT = pagosT(page, userT)
    an = Anuncio(page, userU)
    sol = solicitud(page, userT)
    solU = solicitudes(page, userU)
#----------------Métodos----------------------------
#Método que maneja la barra de los usuarios
    def barra (e):
        if(page.drawer.selected_index==0):
            animate(li)
        if(page.drawer.selected_index==1):
            animate(dU)
            dU.intcomp(userU)
        if(page.drawer.selected_index==2):
            animate(pa)
            pa.yo=I.use()
            pa.princ.controls.clear()
            pa.lista()
        if(page.drawer.selected_index==3):
            animate(solU)
            solU.yo=I.use()
            solU.princ.controls.clear()
            solU.lista()
        if(page.drawer.selected_index==5):
            page.window_close()
#Método que maneja la barra lateral de los trabajadores 
    def barra2 (e):
        if(page.end_drawer.selected_index==0):
            animate(dT)
            dT.intcomp(userT)
        if(page.end_drawer.selected_index==1):
            animate(sol)
            sol.yo=d.use()
            sol.princ.controls.clear()
            sol.lista()
        if(page.end_drawer.selected_index==2):
            animate(paT)
            paT.yo=d.use()
            paT.princ.controls.clear()
            paT.lista()
        if(page.end_drawer.selected_index==4):
            page.window_close()
    #Animaciones de transición
    def animate(con):
        c.content = con
        c.update()
    def mainU(e):
        animate(I)
    def mainT(e):
        animate(d)
    def inT(e):
        userr =d.use()
        passw = d.contra()
        result = buscarT.buscar(userr, passw)
        if(result == True):
            ISC()
            global UserT
            UserT=d.use()
            animate(dT)
            dT.intcomp(userr)
        else:
            ISI()
    def inU(a):
        user =I.use()
        passw = I.contra()
        result = buscarU.buscar(user, passw)
        an.yo= user
        if(result == True):
            ISC()
            global userU
            userU=user
            animate(li)
            li.lista(listar)
        else:
            ISI()
    def regT1(e):
        animate(b)
        b.animateText()
    def regU1(s):
        animate(e)
        e.animateText()
    def ISC():
        page.dialog = dlg
        dlg.open = True
        page.update()
    def ISI():
        page.dialog = dlg2
        dlg2.open = True
        page.update()
    def BIST(e):
        animate(d)
    def BISU(e):
        animate(I)
    def listar( a):
        animate(an)
        an.lista(a)
#--------------------Botones-----------------------
    a.btn2.on_click=mainU
    a.btn1.on_click=mainT
    d.btn1.on_click=inT
    I.btn1.on_click=inU
    d.cont.on_click=regT1
    I.cont.on_click=regU1
    b.buttonb.on_click=BIST
    e.buttonb.on_click=BISU
#---------------------Elementos-----------------------
    dlg = ft.AlertDialog(
        title=ft.Text("¡Inicio de sesión exitoso!") #Ventana que dice si el inicio de sesión fue éxitoso o no.
    )
    dlg2 = ft.AlertDialog(
        title=ft.Text("Usuario o contraseña incorrecta.")
    )
    #Barra lateral Usuario
    page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Inicio",
                    icon=ft.icons.HOME,
                    selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PERSON),
                    label="Perfil",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                    label="Pagos",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                    label="Bandeja",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.OUTBOX),
                    label="Cerrar sesión.",
                    selected_icon=ft.icons.PHONE,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                    label="Salir",
                    selected_icon=ft.icons.PHONE
                ),
            ],
            on_change= barra
        )
    #Barra lateral Empleado
    page.end_drawer= ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Perfil",
                    icon=ft.icons.HOME,
                    selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PERSON),
                    label="Solicitudes",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                    label="Pagos",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.OUTBOX),
                    label="Cerrar sesión",
                    selected_icon=ft.icons.PHONE,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                    label="Salir",
                    selected_icon=ft.icons.PHONE
                ),
            ],
            on_change= barra2
        )
    #Cuando el contenido del switcher cambia, se produce una animación
    c = ft.AnimatedSwitcher(
        content=(a),
        transition=ft.AnimatedSwitcherTransition.SCALE ,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.ELASTIC_IN,
    )
    

#---------Add------------------- 
#Acá va el contenido que tiene la página
    page.add(
        c
    )
    a.animate()
ft.app(target=main)