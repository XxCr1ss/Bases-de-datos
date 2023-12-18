import sqlite3

class ISST():

    def buscar(user, contra):
        ok = False
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                # Ejemplo de inserción de datos en una tabla llamada 'Personas'
            # Confirmar la transacción
                conn.commit()
                usere = (user, contra)
                cursor.execute('''SELECT Usuario, Contraseña from trabajador where Usuario=? AND Contraseña= ?;''', usere)
                resultado =cursor.fetchone()
                if resultado:
                    ok = True
                else:
                    ok = False
        finally:

            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
        return ok
            