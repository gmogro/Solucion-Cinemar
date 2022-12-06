import sqlite3
from sqlite3 import Error
from creando_bdd import create_connection


def select_all_table(conn, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    return rows


def select_row_by_id(conn, table, id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param table: table name
    :param id: id to find in table
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE {'id_' + table} = {id}")

    rows = cur.fetchall()

    return rows


def main():
    database = "Cinemark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query table by id:")
        consulta1 = select_row_by_id(conn, 'usuario', 1)
        print(consulta1)

        print("2. Query all table:")
        consulta2 = select_all_table(conn, 'butaca')
        print(consulta2)


if __name__ == '__main__':
    # main()
    pass
