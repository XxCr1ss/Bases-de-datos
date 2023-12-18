import pymysql

class ISSU():

    def buscar(user, contra):
        conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
        ok = False
        try:
            with conn.cursor() as cursor:
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
            # Confirmar la transacción
                conn.commit()
                usere = (user, contra)
                cursor.execute("SELECT User, Contrasena from `art`.`usuario` where User=%s AND Contrasena= %s;", usere)
                resultado =cursor.fetchone()
                if resultado:
                    ok = True
                else:
                    ok = False
        finally:

            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
        return ok
            