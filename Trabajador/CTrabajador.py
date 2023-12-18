import pymysql
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
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "INSERT INTO `art`.`trabajador` (`Usuario`, `Cedula`, `Nombre`, `Apellido`, `Contraseña`, `Telefono`, `Imagen`, `Precio`) VALUES (%s, %s, %s, %s, %s, %s, %s,%s);"
                sql2 = "INSERT INTO `art`.`anuncio` (`User`, `Profesion`) VALUES (%s, %s);"

                val = (self.usuario, m, self.nombre, self.apellido, self.contrasena, self.telefono, n, self.precio)
                val2 = (self.usuario, self.profeciones)
                cursor.execute(sql, val)
                cursor.execute(sql2, val2)
            # Confirmar la transacción
                conn.commit()
                cursor.execute("select * from trabajador")
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
            