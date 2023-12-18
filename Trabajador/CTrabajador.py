import sqlite3
#Clase que agrega a los trabajadores
class cTrabajador():

    def __init__(self, usuario, cedula, nombre, apellido, contrasena, telefono, imagen, precio, profesiones) -> None:
        self.usuario=usuario
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.contrasena=contrasena
        self.telefono=telefono
        self.imagen=imagen
        self.precio=precio
        self.profeciones = profesiones
    def llenar(self):
        with open(self.cedula, 'rb') as f:
            m=f.read()
        with open(self.imagen, 'rb') as f:
            n=f.read()
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql2 = '''INSERT INTO anuncio (User, Profesion) VALUES (?, ?);'''

                val = (self.usuario, m, self.nombre, self.apellido, self.contrasena, self.telefono, n, self.precio)
                val2 = (self.usuario, self.profeciones)
                cursor.execute('''
                INSERT INTO trabajador (Usuario, Cedula, Nombre, Apellido, Contraseña, Telefono, Imagen, Precio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   ''', val)
                cursor.execute(sql2, val2)
            # Confirmar la transacción
                conn.commit()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
            