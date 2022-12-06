import sqlite3
from sqlite3 import Error
from BDD.creando_bdd import create_connection


def create_tipo_pelicula(conn, tipo_pelicula):
    """
    Create a new project into the projects table
    :param conn: object of type sqlite3.Connection
    :param descuento:list of values
    :return: descuento id
    """
    sql = ''' INSERT INTO tipo_pelicula(formato, idioma, subtitulada)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tipo_pelicula)
    conn.commit()
    return cur.lastrowid


def create_clasificacion_pelicula(conn, clasificacion_pelicula):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param localidad: list of values
    :return:
    """
    sql = ''' INSERT INTO clasificacion_pelicula(identificador, recomendacion, descripcion)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, clasificacion_pelicula)
    conn.commit()
    return cur.lastrowid


def create_pelicula(conn, pelicula):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tipo: list of values
    :return:
    """
    sql = ''' INSERT INTO pelicula(nombre, sinopsis, descripcion, duracion, id_tipo_pelicula, id_clasificacion)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()
    return cur.lastrowid


def create_descuento(conn, descuento):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param domicilio: list of values
    :return:
    """
    sql = ''' INSERT INTO descuento(dia, porcentaje)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    return cur.lastrowid

def create_producto(conn, producto):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param producto: list of values
    :return:
    """
    sql = ''' INSERT INTO producto(nombre, marca, fecha_venc, precio, stock, id_tipo)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, producto)
    conn.commit()
    return cur.lastrowid

def create_usuario(conn, usuario):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param usuario: list of values
    :return:
    """
    sql = ''' INSERT INTO usuario(nombre, apellido, email, dni, fecha_nacimiento, username, password, tipo)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid


def create_tarjeta_credito(conn, tarjeta_credito):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tarjeta_credito: list of values
    :return:
    """
    sql = ''' INSERT INTO tarjeta_credito(numero, banco, titular, fecha_caducidad, codigo_seguridad, id_usuario)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tarjeta_credito)
    conn.commit()
    return cur.lastrowid


def create_sala(conn, sala):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO sala(numero, formato, capacidad)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sala)
    conn.commit()
    return cur.lastrowid


def create_butaca(conn, butaca):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO butaca(fila, numero, reservada, id_sala)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()
    return cur.lastrowid


def create_sesion(conn, sesion):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO sesion(fecha, hora, id_sala, id_pelicula)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sesion)
    conn.commit()
    return cur.lastrowid


def create_reserva(conn, reserva):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO reserva(precio, fecha, id_sesion, id_butaca, id_usuario, id_tarjeta, id_descuento)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()
    return cur.lastrowid


def insert_data(database):

    tipo_peliculas = [
        ['2D', "Español", "No"],
        ['2D', "Ingles", "Si"],
        ["2D", "Ingles", "No"],
        ['3D', "Español", "No"],
        ["3D", "Ingles", "No"],
        ["3D", "Ingles", "Si"],
        ["4D", "Español", "No"],
        ["4D", "Ingles", "No"],
        ["4D", "Ingles", "Si"]
    ]

    clasificacion_peliculas = [
        ["A", "+18", "Violencia extrema"],
        ["B", "+16", "Violencia moderada"],
        ["C", "+13", "Violencia leve"],
        ["D", "+7", "Sin violencia"]
    ]

    peliculas = [
        ["Avengers: Endgame", "El final de una era", "La batalla final", 180, 1, 1],
        ["Avengers: Infinity War", "El final de la mitad", "Thanos destruye la mitad del universo", 200, 2, 2],
        ["Avengers: Age of Ultron", "La era de Ultron", "Ultron se hace con el poder", 190, 3, 1],
        ["Avengers", "Los vengadores", "Los vengadores se unen para salvar el mundo", 210, 4, 2],
        ["Iron Man 1", "El hombre de hierro", "Tony Stark crea el traje de Iron", 180, 5, 3],
        ["Capitan America: Civil War", "Guerra Civil", "Los vengadores se dividen", 180, 6, 1],
        ["Capitan America: The First Avenger", "El primer vengador", "Steve Rogers se convierte en el primer vengador", 180, 1, 2],
        ["Capitan America: The Winter Soldier", "El soldado del invierno", "Steve Rogers se enfrenta a un nuevo villano", 180, 2, 3],
        ["Capitan America: The Winter Soldier", "El soldado del invierno", "Steve Rogers se enfrenta a un nuevo villano", 180, 3, 1],
        ["Iron Man 3", "El hombre de hierro 3", "Tony Stark se enfrenta a un nuevo villano", 180, 4, 2],
        ["Spyder Man", "El hombre araña", "Peter Parker se convierte en el hombre araña", 180, 5, 3],
        ["Spyder Man 2", "El hombre araña 2", "Peter Parker se enfrenta a un nuevo villano", 180, 6, 1]
    ]

    descuentos = [
        ["Lunes", 0.2],
        ["Martes", 0.15],
        ["Miercoles", 0.2],
        ["Jueves", 0.15],
        ["Viernes", 0.1],
        ["Sabado", 0.1],
        ["Domingo", 0.1]
    ]

    usuarios = [
        ['Jose', 'Perez', 'jose_perez@gmail.com',
         '12345678', '2020-01-01',  'jose_perez', '123456abcd#', 'admin'],
        ['Tony', 'Stark', 'tony_stark@gmail.com',
         '11223344', '2000-01-01',  'tony_stark', 'jarvis1234', 'admin'],
        ['Julian', 'Alvarez', 'july_alvarez@gmail.com',
         '11122233', '1998-01-01', 'juli_alvarez', 'julian1234', 'cliente'],
        ['Peter', 'Parker', 'spyder_man@gmail.com',
         '11112222', '2002-01-01', 'la_araña', 'spyder1234', 'cliente'],
        ["Lionel", "Messi", "leo_messi@gmail.com",
         "12121212", '2002-01-01',  'la_pulga', 'leo1234', 'cliente'],
        ["Cristiano", "Ronaldo", "el_bicho@gmail.com",
         "21212121", '2002-01-01', 'el_bicho', 'cristiano1234', 'cliente'],
        ["Marcelo", "Gallardo", "muñeco_gallardo@gmail.com",
         "34343434", '2002-01-01',  'muñeco', 'gallardo1234', 'admin']
    ]

    tarjetas_credito = [
        ['123456789', 'Banco 1', 'jose_perez', '2020-01-01', '123', 1],
        ['987654321', 'Banco 2', 'tony_stark', '2020-01-01', '123', 2],
        ['111222333', 'Banco 3', 'juli_alvarez', '2020-01-01', '123', 3],
        ['444555666', 'Banco 4', 'la_araña', '2020-01-01', '123', 4],
        ['777888999', 'Banco 5', 'la_pulga', '2020-01-01', '123', 5],
        ['000111222', 'Banco 6', 'el_bicho', '2020-01-01', '123', 6],
    ]

    salas = [
        ["1", "2D", 10],
        ["2", "3D", 10],
        ["3", "2D", 10],
        ["4", "3D", 10],
        ["5", "2D", 10],
        ["6", "4D", 10],
        ["7", "4D", 10],
    ]

    butacas = [
        # sala 1
        ["A", 1, "No", 1],
        ["A", 2, "No", 1],
        ["A", 3, "No", 1],
        ["A", 4, "No", 1],
        ["A", 5, "No", 1],
        ["B", 1, "No", 1],
        ["B", 2, "No", 1],
        ["B", 3, "No", 1],
        ["B", 4, "No", 1],
        ["B", 5, "No", 1],
        # sala 2
        ["A", 1, "No", 2],
        ["A", 2, "No", 2],
        ["A", 3, "No", 2],
        ["A", 4, "No", 2],
        ["A", 5, "No", 2],
        ["B", 1, "No", 2],
        ["B", 2, "No", 2],
        ["B", 3, "No", 2],
        ["B", 4, "No", 2],
        ["B", 5, "No", 2],
        # sala 3
        ["A", 1, "No", 3],
        ["A", 2, "No", 3],
        ["A", 3, "No", 3],
        ["A", 4, "No", 3],
        ["A", 5, "No", 3],
        ["B", 1, "No", 3],
        ["B", 2, "No", 3],
        ["B", 3, "No", 3],
        ["B", 4, "No", 3],
        ["B", 5, "No", 3],
        # sala 4
        ["A", 1, "No", 4],
        ["A", 2, "No", 4],
        ["A", 3, "No", 4],
        ["A", 4, "No", 4],
        ["A", 5, "No", 4],
        ["B", 1, "No", 4],
        ["B", 2, "No", 4],
        ["B", 3, "No", 4],
        ["B", 4, "No", 4],
        ["B", 5, "No", 4],
        # sala 5
        ["A", 1, "No", 5],
        ["A", 2, "No", 5],
        ["A", 3, "No", 5],
        ["A", 4, "No", 5],
        ["A", 5, "No", 5],
        ["B", 1, "No", 5],
        ["B", 2, "No", 5],
        ["B", 3, "No", 5],
        ["B", 4, "No", 5],
        ["B", 5, "No", 5],
    ]

    sesiones = [
        ["2020-01-01", "12:00:00", 1, 1],
        ["2020-01-01", "15:00:00", 2, 1],
        ["2020-01-01", "18:00:00", 3, 1],
        ["2020-01-01", "21:00:00", 4, 1],
        ["2020-01-02", "12:00:00", 1, 2],
        ["2020-01-02", "15:00:00", 2, 2],
        ["2020-01-02", "18:00:00", 3, 2],
        ["2020-01-02", "21:00:00", 4, 2],
        ["2020-01-03", "12:00:00", 1, 3],
        ["2020-01-03", "15:00:00", 2, 3],
        ["2020-01-03", "18:00:00", 3, 3],
        ["2020-01-03", "21:00:00", 4, 3],
        ["2020-01-04", "12:00:00", 1, 4],
        ["2020-01-04", "15:00:00", 2, 4],
        ["2020-01-04", "18:00:00", 3, 4],
        ["2020-01-04", "21:00:00", 4, 4],
        ["2020-01-05", "12:00:00", 1, 5],
        ["2020-01-05", "15:00:00", 2, 5],
        ["2020-01-05", "18:00:00", 3, 5],
        ["2020-01-05", "21:00:00", 4, 5],
        ["2020-01-06", "12:00:00", 1, 6],
        ["2020-01-06", "15:00:00", 2, 6],
        ["2020-01-06", "18:00:00", 3, 6],
        ["2020-01-06", "21:00:00", 4, 6],
        ["2020-01-07", "12:00:00", 1, 7],
        ["2020-01-07", "15:00:00", 2, 7],
        ["2020-01-07", "18:00:00", 3, 7],
        ["2020-01-07", "21:00:00", 4, 7],
        ["2020-01-08", "12:00:00", 1, 8],
        ["2020-01-08", "15:00:00", 2, 8],
        ["2020-01-08", "18:00:00", 3, 8],
        ["2020-01-08", "21:00:00", 4, 8],
        ["2020-01-09", "12:00:00", 1, 9],
        ["2020-01-09", "15:00:00", 2, 9],
        ["2020-01-09", "18:00:00", 3, 9],
        ["2020-01-09", "21:00:00", 4, 9],
        ["2020-01-10", "12:00:00", 1, 10],
        ["2020-01-10", "15:00:00", 2, 10],
        ["2020-01-10", "18:00:00", 3, 10],
        ["2020-01-10", "21:00:00", 4, 10],
        ["2020-01-11", "12:00:00", 1, 11],
        ["2020-01-11", "15:00:00", 2, 11],
        ["2020-01-11", "18:00:00", 3, 11],
        ["2020-01-11", "21:00:00", 4, 11],
        ["2020-01-12", "12:00:00", 1, 12],
        ["2020-01-12", "15:00:00", 2, 12],
        ["2020-01-12", "18:00:00", 3, 12],
        ["2020-01-12", "21:00:00", 4, 12],
    ]
    # precio, fecha, id_sesion, id_butaca, id_usuario, id_tarjeta, id_descuento
    reservas = [
        [500, "2020-01-01", 1, 1, 1, 1, 1],
        [500, "2020-01-01", 1, 2, 1, 1, 1],
        [500, "2020-01-01", 2, 1, 2, 2, 2],
        [500, "2020-01-01", 2, 2, 2, 2, 2],
        [500, "2020-01-01", 3, 1, 3, 3, 3],
        [500, "2020-01-01", 3, 2, 3, 3, 3],
        [500, "2020-01-01", 4, 1, 4, 4, 4],
        [500, "2020-01-01", 4, 2, 4, 4, 4],
        [500, "2020-01-02", 5, 1, 5, 5, 5],
        [500, "2020-01-02", 5, 2, 5, 5, 5],
        [500, "2020-01-02", 6, 1, 6, 6, 6],
        [500, "2020-01-02", 6, 2, 6, 6, 6],
        [500, "2020-01-02", 7, 1, 7, 7, 7],
        [500, "2020-01-02", 7, 2, 7, 7, 7],
    ]

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new descuento
        for tipo_pelicula in tipo_peliculas:
            create_tipo_pelicula(conn, tipo_pelicula)

        # create a new localidad
        for clasificacion in clasificacion_peliculas:
            create_clasificacion_pelicula(conn, clasificacion)

        # create a new pelicula
        for pelicula in peliculas:
            create_pelicula(conn, pelicula)

        # create a new descuento
        for descuento in descuentos:
            create_descuento(conn, descuento)

        # create a new usuario
        for usuario in usuarios:
            create_usuario(conn, usuario)

        # create a new tarjeta_credito
        for tarjeta in tarjetas_credito:
            create_tarjeta_credito(conn, tarjeta)

        # create a new sala
        for sala in salas:
            create_sala(conn, sala)

        # create a new butaca
        for butaca in butacas:
            create_butaca(conn, butaca)

        # create a new sesion
        for sesion in sesiones:
            create_sesion(conn, sesion)

        # create a new reserva
        for reserva in reservas:
            create_reserva(conn, reserva)

        print("Valores insertados")


if __name__ == '__main__':
    # insert_data("Cinemark.db")
    pass
