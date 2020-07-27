import sqlite3

def connection():
    conn = sqlite3.connect("dbaddressbook")
    return conn
def crearDB():

    micursor = connection().cursor()
    micursor.execute("""
    create table contactos(
    idcontacto integer primary key autoincrement,
    name varchar(30),
    phono varchar(10),
    info varchar(100))    
    
    """)
    connection().close()


def insertarDB(contactos):
    con = connection()
    cursor = con.cursor()
    cursor.execute("insert into contactos values (NULL,?,?,?)",(contactos))
    con.commit()
    con.close()

def eliminarDato(idselect):
    con = connection()
    cursor = con.cursor()
    cursor.execute("delete from contactos where idcontacto = {}".format(idselect))
    con.commit()
    con.close()

def editarDato(contactos):
    con = connection()
    cursor = con.cursor()
    cursor.execute("update contactos set name=?, phono=? , info=?  where idcontacto=?",(contactos))
    con.commit()
    con.close()

def mostrarDB():
    cursor = connection().cursor()
    select = cursor.execute("SELECT *FROM contactos")
    connection().close()
    return select

def mostrarDBDesc():
    cursor = connection().cursor()
    select = cursor.execute("SELECT *FROM contactos order by idcontacto desc")
    connection().close()
    return select