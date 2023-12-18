import sqlite3

class ISSU():

    def buscar(user, contra):
        ok = False
        conn = sqlite3.connect("mibase.db")
        try:
                cursor = conn.cursor()
                conn.commit()
                usere = (user, contra)
                cursor.execute('''SELECT User, Contrasena from usuario where User=? AND Contrasena= ?;''', usere)
                resultado =cursor.fetchone()
                if resultado:
                    ok = True
                else:
                    ok = False
        finally:

            # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
            conn.close()
        return ok
            