import sqlite3

class cUsuario():

    def __init__(self, usuario, nombre, apellido, direccion, contrasena, tarjeta, recibo, imagen,  telefono, fecha,  CVC) -> None:
        self.usuarrio=usuario
        self.tarjetta=tarjeta
        self.nombrre=nombre
        self.apelllido=apellido
        self.contrasenna=contrasena
        self.tellefono=telefono
        self.imaggen=imagen
        self.recibbo=recibo
        self.cvv = CVC
        self.fechha = fecha
        self.add = direccion
    def llenar(self):
        with open(self.recibbo, 'rb') as f:
            m=f.read()
        with open(self.imaggen, 'rb') as f:
            n=f.read()
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'

                val = (self.usuarrio, self.nombrre, self.apelllido, self.add, self.contrasenna, self.tarjetta, m, n, self.tellefono, self.fechha, self.cvv)
                cursor.execute('''INSERT INTO usuario (User, Nombre, Apellido, Direccion, Contrasena, Tarjeta, Recibo, Foto, Celular, [Fecha vencimiento], CVC) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', val)
            # Confirmar la transacción
                conn.commit()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
            