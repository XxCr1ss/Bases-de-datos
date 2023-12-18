# import required libraries
import pymysql

# read an image
def opem(imagen: str):
    with open(imagen, 'rb') as f:
        m=f.read()
    return m
def imagen(g):
    with open('zz.jpg', 'wb') as q:
        q.write(g)
 
# printing shape of image


conn = pymysql.connect(host='localhost', user='root', password = 'rafael123', db='art')
try:
    with conn.cursor() as cursor:
            # Ejemplo de inserción de datos en una tabla llamada 'Personas'
        # sql = "insert into img (Name, Img) values (1, %s)"
            #cursor.execute(sql, imageToMatrice)
        # Confirmar la transacción
        #conn.commit()
        cursor.execute('select * from img')
        nombre, img = cursor.fetchone()
        imagen(img)
     
finally:
    # Cerrar la conexión, independientemente de si la transacción fue exitosa o no
    conn.close()