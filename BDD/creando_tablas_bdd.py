import sqlite3
from BDD.creando_bdd import create_connection


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def creando_tablas(database):

    sql_create_tipo_pelicula_table = """ CREATE TABLE IF NOT EXISTS tipo_pelicula (
                                        id_tipo_pelicula integer PRIMARY KEY AUTOINCREMENT,
                                        formato text NOT NULL,
                                        idioma text NOT NULL,
                                        subtitulada text NOT NULL
                                    ); """

    sql_create_clasificacion_pelicula_table = """CREATE TABLE IF NOT EXISTS clasificacion_pelicula (
                                    id_clasificacion integer PRIMARY KEY AUTOINCREMENT,
                                    identificador text NOT NULL,
                                    recomendacion text NOT NULL,
                                    descripcion text NOT NULL
                                );"""

    sql_create_pelicula_table = """CREATE TABLE IF NOT EXISTS pelicula (
                                id_pelicula integer PRIMARY KEY AUTOINCREMENT,
                                nombre text NOT NULL,
                                sinopsis text NOT NULL,
                                descripcion text NOT NULL,
                                duracion integer NOT NULL,
                                id_tipo_pelicula integer NOT NULL,
                                id_clasificacion integer NOT NULL,
                                FOREIGN KEY (id_tipo_pelicula) REFERENCES tipo_pelicula (id_tipo_pelicula),
                                FOREIGN KEY (id_clasificacion) REFERENCES clasificacion_pelicula (id_clasificacion)
                            );"""

    sql_create_descuento_table = """CREATE TABLE IF NOT EXISTS descuento (
                                id_descuento integer PRIMARY KEY AUTOINCREMENT,
                                dia integer NOT NULL,
                                porcentaje text NOT NULL
                            );"""

    sql_create_usuario_table = """CREATE TABLE IF NOT EXISTS usuario (
                                id_usuario integer PRIMARY KEY AUTOINCREMENT,
                                nombre text NOT NULL,
                                apellido text DEFAULT NULL,
                                email text NOT NULL,
                                dni text NOT NULL,
                                fecha_nacimiento text NOT NULL,
                                username text DEFAULT NULL,
                                password text DEFAULT NULL,
                                tipo text NOT NULL
                            );"""

    sql_create_tarjeta_credito_table = """CREATE TABLE IF NOT EXISTS tarjeta_credito (
                                id_tarjeta integer PRIMARY KEY AUTOINCREMENT,
                                numero integer NOT NULL,
                                banco text DEFAULT NULL,
                                titular text NOT NULL,
                                fecha_caducidad text NOT NULL,
                                codigo_seguridad text DEFAULT NULL,
                                id_usuario integer NOT NULL,
                                FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
                            );"""

    sql_create_sala_table = """CREATE TABLE IF NOT EXISTS sala (
                                id_sala integer PRIMARY KEY AUTOINCREMENT,
                                numero integer NOT NULL,
                                formato text NOT NULL,
                                capacidad text NOT NULL
                            );"""

    sql_create_butaca_table = """CREATE TABLE IF NOT EXISTS butaca (
                                id_butaca integer PRIMARY KEY AUTOINCREMENT,
                                fila text NOT NULL,
                                numero text NOT NULL,
                                reservada text NOT NULL,
                                id_sala integer NOT NULL,
                                FOREIGN KEY (id_sala) REFERENCES sala (id_sala)
                            );"""

    sql_create_sesion_table = """CREATE TABLE IF NOT EXISTS sesion (
                                id_sesion integer PRIMARY KEY AUTOINCREMENT,
                                fecha text NOT NULL,
                                hora text NOT NULL,
                                id_sala integer NOT NULL,
                                id_pelicula integer NOT NULL,
                                FOREIGN KEY (id_sala) REFERENCES sala (id_sala),
                                FOREIGN KEY (id_pelicula) REFERENCES pelicula (id_pelicula)
                            );"""

    sql_create_reserva_table = """CREATE TABLE IF NOT EXISTS reserva (
                                id_reserva integer PRIMARY KEY AUTOINCREMENT,
                                precio integer NOT NULL,
                                fecha text NOT NULL,
                                id_sesion integer NOT NULL,
                                id_butaca integer NOT NULL,
                                id_usuario integer NOT NULL,
                                id_tarjeta integer NOT NULL,
                                id_descuento integer NOT NULL,
                                FOREIGN KEY (id_sesion) REFERENCES sesion (id_sesion),
                                FOREIGN KEY (id_butaca) REFERENCES butaca (id_butaca),
                                FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
                                FOREIGN KEY (id_tarjeta) REFERENCES tarjeta_credito (id_tarjeta),
                                FOREIGN KEY (id_descuento) REFERENCES descuento (id_descuento)
                            );"""
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        list_table = [
            "tipo_pelicula",
            "clasificacion_pelicula",
            "pelicula",
            "descuento",
            "usuario",
            "tarjeta_credito",
            "sala",
            "butaca",
            "sesion",
            "reserva"
        ]
        # create projects table
        for table in list_table:
            create_table(conn, eval(f"sql_create_{table}_table"))
        print("Tablas creadas")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    # creando_tablas("Cinemark.db")
    pass
