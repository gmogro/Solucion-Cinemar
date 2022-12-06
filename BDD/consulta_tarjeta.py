import sqlite3
from sqlite3 import Error
from creando_bdd import create_connection


def select_tarjeta(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection objects
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito")

    rows = cur.fetchall()

    return rows


def select_tarjeta_numero(conn, numero):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param numero:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE numero = ?", (numero,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_bancaria(conn, banco):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param banco:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE banco = ?", (banco,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_titular(conn, titular):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param titular:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE titular = ?", (titular,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_fecha(conn, fecha):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param fecha:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE fecha_caducidad = ?", (fecha,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_cvv(conn, cvv):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param cvv:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE codigo_seguridad = ?", (cvv,))

    rows = cur.fetchall()

    return rows


def datos_usuario_tarjeta(conn, id_usuario):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param id_usuario:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE id_usuario = ?", (id_usuario,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_id(conn, id_tarjeta):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param id_tarjeta:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE id_tarjeta = ?", (id_tarjeta,))

    rows = cur.fetchall()

    return rows


def select_tarjeta_id_usuario(conn, id_usuario):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param id_usuario:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE id_usuario = ?", (id_usuario,))

    rows = cur.fetchall()

    return rows 


def select_tarjeta_vencida(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE date(fecha_caducidad) <= date('now')")

    rows = cur.fetchall()

    return rows


def select_tarjeta_a_vencer(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM tarjeta_credito WHERE date(fecha_caducidad) BETWEEN '{date.today()}' AND '{date.today() + timedelta(days = 60)}'")

    rows = cur.fetchall()

    return rows


def comprobar_tarjeta(conn, numero, cvv):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarjeta_credito WHERE numero = ? AND codigo_seguridad = ?", (numero, cvv))

    rows = cur.fetchall()

    return rows


def main():
    database = "Cinemark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Consultas de tarjetas")


if __name__ == '__main__':
    # main()
    pass

