import sqlite3
from sqlite3 import Error
from BDD.creando_bdd import create_connection


def delete_row_table_by_id(conn, tabla, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = f'DELETE FROM {tabla} WHERE {"id_" + tabla} = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_table(conn, table):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = "Cinemark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # Delete selected by id row in the table
        delete_row_table_by_id(conn, 'descuento', 1)
        print("Valor por id eliminado")
        # Delete all rows in the table
        delete_all_table(conn, 'localidad')
        print("Todos los registros eliminados")


if __name__ == '__main__':
    # main()
    pass
