import pymysql

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
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
                sql = "INSERT INTO `art`.`usuario` (`User`, `Nombre`, `Apellido`, `Direccion`, `Contrasena`, `Tarjeta`, `Recibo`, `Foto`, `Celular`, `Fecha vencimiento`, `CVC`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

                val = (self.usuarrio, self.nombrre, self.apelllido, self.add, self.contrasenna, self.tarjetta, m, n, self.tellefono, self.fechha, self.cvv)
                cursor.execute(sql, val)
            # Confirmar la transacción
                conn.commit()
        finally:
            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
            