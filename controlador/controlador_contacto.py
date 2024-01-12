from bd import obtener_conexion

def insertar_contacto(nombres,apellidos,web,profesion,telefono,email,foto):
    conexion=obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO CONTACTO (nombre, apellidos, web, profesion, telefono, email, foto) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       (nombres,apellidos,web,profesion,telefono,email,foto) )
    conexion.commit()
    conexion.close()
    
def obtener_contactos():
    conexion=obtener_conexion()
    contactos=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from CONTACTO")
        contactos=cursor.fetchall()
    conexion.close()
    return contactos

def obtener_contactoid(id):
    conexion=obtener_conexion()
    contacto=None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from CONTACTO WHERE id=%s",(id,))
        contacto=cursor.fetchone()
    conexion.close()
    return contacto

def eliminar_contacto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM CONTACTO WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    
def actualizar_contacto(id,nombres,apellidos,web,profesion,telefono,email,foto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE CONTACTO SET nombre = %s, apellidos = %s, web = %s,profesion=%s,telefono=%s,email=%s,foto=%s WHERE id = %s",
                       (nombres,apellidos,web,profesion,telefono,email,foto,id))
    conexion.commit()
    conexion.close()