import sqlite3
from sqlite3 import Error
from BDD.creando_bdd import create_connection


def select_name_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM usuario")

    rows = cur.fetchall()

    return rows


def select_usuario_by_id(conn, id):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE id_usuario = {id}")

    rows = cur.fetchall()

    return rows

def select_apellido_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT apellido FROM usuario")

    rows = cur.fetchall()

    return rows

def select_email_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT email FROM usuario")

    rows = cur.fetchall()

    return rows

def select_dni_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT dni FROM usuario")

    rows = cur.fetchall()

    return rows

def select_username_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT username FROM usuario")

    rows = cur.fetchall()

    return rows

def validate_user(conn, username, password):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE username = ? AND password = ?", (username, password))

    rows = cur.fetchall()

    return True if len(rows) > 0 else False


def valid_user(conn, username):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE username = ?", (username,))

    rows = cur.fetchall()

    return True if len(rows) > 0 else False

def valid_email(conn, email):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE email = ?", (email,))

    rows = cur.fetchall()

    return True if len(rows) > 0 else False

def valid_dni(conn, dni):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE dni = ?", (dni,))

    rows = cur.fetchall()

    return True if len(rows) > 0 else False


def select_tipo_of_user(conn, username):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT tipo FROM usuario WHERE username = ?", (username,))

    rows = cur.fetchall()

    return rows[0][0]


def select_nombre_apellido_dni_email_fecha_nacimiento(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT nombre, apellido, dni, email, fecha_nacimiento FROM usuario")

    rows = cur.fetchall()

    return rows


def select_nombre_id_by_nombre(conn, nombre):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT id_usuario, nombre FROM usuario where nombre = '{}'".format(nombre))

    rows = cur.fetchall()

    return rows


def select_by_username(conn, username):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE username = ?", (username,))

    rows = cur.fetchall()

    return rows


def select_by_email(conn, email):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE email = ?", (email,))

    rows = cur.fetchall()

    return rows


def select_by_dni(conn, dni):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE dni = ?", (dni,))

    rows = cur.fetchall()

    return rows


def select_by_id(conn, id):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE id = ?", (id,))

    rows = cur.fetchall()

    return rows


def select_cantidad_usuarios(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM usuario")

    rows = cur.fetchall()

    return rows


def select_all_usuarios(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_id(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY id")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_username(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY username")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_nombre(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY nombre")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_apellido(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY apellido")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_email(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY email")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_dni(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY dni")

    rows = cur.fetchall()

    return rows


def select_all_usuarios_order_by_fecha_nacimiento(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY fecha_nacimiento")

    rows = cur.fetchall()

    return rows


def main():
    database = "Cinemark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        pass


if __name__ == '__main__':
    # main()
    pass
