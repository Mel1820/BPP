import sqlite3
from sqlite3  import Error
from sqlite3.dbapi2 import Cursor

def conexion_sql():
    """
    Conexion  SQL. Es una funcion que sirve para crear una BBDD.
        >>>con = sqlite3.connect('./lec7.db')
        >>>print('La BBDD se creo con exito!')
        >>>return con
    En el caso  que no se cree correctamente se mostrar un Error
    """
    try:
        con = sqlite3.connect('./lec7.db')
        print('La BBDD se creo con exito!')
        return con
    except Error:
        print(Error)

#funcion para crear una tabla en nuestra BBDD de 4 campos
def crear_tabla_alumnos(con):
    """
    Crear tabla alumnas. Es una funcion a la cual le pasamos la conexion
    sql y creamos una tabla llamada ALUMNOS con 4 columas:
        >>>cursor =con.cursor()
        >>>cursor.execute('''CREATE TABLE alumnos(
            >>>id integer primary key,
            >>>nombre text,
            >>>telefono varchar,
            >>>email varchar)''')
        >>>con.commit()
    Si algo sale mal en el proceso se mostrar un Error
    """
    try:
        cursor =con.cursor()
        cursor.execute("""CREATE TABLE alumnos(
            id integer primary key,
            nombre text,
            telefono varchar,
            email varchar)""")
        con.commit()
        print("La tabla alumnos se creo correctamente")
    except Error:
        print(Error)

#funcion para insertar datos en la tabla de alumnos
def insertar(con, datos):
    """
    Insertar. Es una funcion para insertar datos en nuestra tabla.
    Primero le pasamos la conexion y luego los datos
        >>>cursor =con.cursor()
        >>>cursor =con.cursor()
        >>>cursor.execute('''INSERT INTO alumnos(id,nombre,telefono,email )
        >>>VALUES(?,?,?,?)''', datos)
        >>>con.commit()
    Si algo sale mal en el proceso se mostrar un Error
    """
    try:
        cursor =con.cursor()
        cursor.execute("""INSERT INTO alumnos(id,nombre,telefono,email )
        VALUES(?,?,?,?)""", datos)
        con.commit()
        print("Los datos se han insertado correctamente")
    except Error:
        print(Error)

#funcion para actualizar datos en la tabla 
def actualizar(con, datos):
    """
    Actualizar. Es una funcion para actualizar los datos en nuestra tabla.
    Le pasamos la conexion y luego los datos
        >>>cursor =con.cursor()
        >>>cursor.execute('''UPDATE ? 
                        >>>SET id= ?,nombre = ?,telefono = ?,email = ?''', datos)
        >>>con.commit()
    Si algo sale mal en el proceso se mostrar un Error
    """
    try:
        cursor =con.cursor()
        cursor.execute("""UPDATE ? 
                            SET id= ?,nombre = ?,telefono = ?,email = ?""", datos)
        con.commit()
        print("Los datos se han actualizado")
    except Error:
        print(Error)

#funcion para borrar datos en la tabla 
def borrar(con, datos):
    """
    Borrar. Es una funcion para borrar datos en nuestra tabla.
    Pasamos la conexion y luego el dato q queremos eliminar
        >>>cursor =con.cursor()
        >>>cursor.execute('''DELETE FROM ? WHERE id=?''', datos)
        >>>con.commit()
    Si algo sale mal en el proceso se mostrar un Error
    """
    try:
        cursor =con.cursor()
        cursor.execute("""DELETE FROM ? WHERE id=?""", datos)
        con.commit()
        print("Se ha eliminado correctamente")
    except Error:
        print(Error)

#llamadas a las funciones        
con = conexion_sql()
crear_tabla_alumnos(con)

