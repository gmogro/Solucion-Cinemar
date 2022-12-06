import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def update_descuento(conn, descuento):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param descuento:
    :return: project id
    """
    sql = ''' UPDATE descuento
                SET dia = ?, porcentaje = ?
                WHERE id_descuento = ?'''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()


def update_atributo_descuento(conn, atributo ,descuento):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param descuento:
    :return: project id
    """
    sql = f''' UPDATE descuento 
                SET {atributo} = ?
                WHERE id_descuento = ?'''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()


def update_usuario(conn, usuario):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param usuario:
    :return: project id
    """
    sql = ''' UPDATE usuario
              SET nombre = ?, apellido = ?, email = ?, dni = ?, fecha_nacimiento = ?, username = ?, password = ?, tipo= ?
              WHERE id_usuario = ?'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()


def update_atributo_usuario(conn, atributo, usuario):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param usuario:
    :return: project id
    """
    sql = f''' UPDATE usuario
                SET {atributo} = ?
                WHERE id_usuario = ?'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()


def update_tarjeta(conn, tarjeta):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param tarjeta:
    :return: project id
    """
    sql = ''' UPDATE tarjeta_credito
              SET numero = ?, banco = ?, titular = ?, fecha_caducidad = ?, codigo_seguridad = ?, id_usuario = ?
              WHERE id_tarjeta = ?'''
    cur = conn.cursor()
    cur.execute(sql, tarjeta)
    conn.commit()


def update_atributo_tarjeta(conn, atributo, tarjeta):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param tarjeta:
    :return: project id
    """
    sql = f''' UPDATE tarjeta_credito
                SET {atributo} = ?
                WHERE id_tarjeta = ?'''
    cur = conn.cursor()
    cur.execute(sql, tarjeta)
    conn.commit()


def update_tipo_pelicula(conn, tipo_pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE tipo_pelicula
              SET formato = ?, idioma = ?, subtitulada = ?
              WHERE id_tipo_pelicula = ?'''
    cur = conn.cursor()
    cur.execute(sql, tipo_pelicula)
    conn.commit()


def update_atributo_tipo_pelicula(conn, atributo ,tipo_pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE tipo_pelicula
                SET {atributo} = ? 
                WHERE id_tipo_pelicula = ?'''
    cur = conn.cursor()
    cur.execute(sql, tipo_pelicula)
    conn.commit()


def update_clasificacion_pelicula(conn, clasificacion_pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE clasificacion_pelicula
              SET identificador = ?, recomendacion = ?, descripcion = ?
              WHERE id_clasificacion = ?'''
    cur = conn.cursor()
    cur.execute(sql, clasificacion_pelicula)
    conn.commit()


def update_atributo_clasificacion_pelicula(conn, atributo ,clasificacion_pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE clasificacion_pelicula
                SET {atributo} = ?
                WHERE id_clasificacion = ?'''
    cur = conn.cursor()
    cur.execute(sql, clasificacion_pelicula)
    conn.commit()


def update_pelicula(conn, pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE pelicula
              SET nombre = ?, sinopsis = ?,descripcion = ?, duracion = ?, id_tipo_pelicula = ?, id_clasificacion = ?
              WHERE id_pelicula = ?'''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()


def update_atributo_pelicula(conn, atributo, pelicula):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE pelicula
                SET {atributo} = ?
                WHERE id_pelicula = ?'''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()


def update_sala(conn, sala):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE sala
              SET numero = ?, formato = ?, capacidad = ?
              WHERE id_sala = ?'''
    cur = conn.cursor()
    cur.execute(sql, sala)
    conn.commit()


def update_atributo_sala(conn, atributo, sala):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE sala
                SET {atributo} = ?
                WHERE id_sala = ?'''
    cur = conn.cursor()
    cur.execute(sql, sala)
    conn.commit()


def update_butaca(conn, butaca):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE butaca
              SET fila = ?, numero = ?, reservada = ?, id_sala = ?
              WHERE id_butaca = ?'''
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()


def update_atributo_butaca(conn, atributo, butaca):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE butaca
                SET {atributo} = ?
                WHERE id_butaca = ?'''
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()


def update_sesion(conn, sesion):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE sesion
              SET fecha = ?, hora = ?, id_sala = ?, id_pelicula = ?
              WHERE id_sesion = ?'''
    cur = conn.cursor()
    cur.execute(sql, sesion)
    conn.commit()


def update_atributo_sesion(conn, atributo, sesion):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE sesion
                SET {atributo} = ?
                WHERE id_sesion = ?'''
    cur = conn.cursor()
    cur.execute(sql, sesion)
    conn.commit()


def update_reserva(conn, reserva):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = ''' UPDATE reserva
              SET precio = ?, fecha = ?, id_sesion = ?, id_butaca = ?, id_usuario = ?, id_tarjeta = ?, id_descuento = ?
              WHERE id_reserva = ?'''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()


def update_atributo_reserva(conn, atributo, reserva):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param comprobante:
    :return: project id
    """
    sql = f''' UPDATE reserva
                SET {atributo} = ?
                WHERE id_reserva = ?'''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()


def main():
    database = "Cinemark.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        # actualizar tipo_pelicula
        update_tipo_pelicula(conn, ('3D', "Ingles", "Si", 1))
        update_atributo_tipo_pelicula(conn, 'idioma', ('Frances', 2))

        # actualizar clasificacion pelicula
        update_clasificacion_pelicula(conn, ('E',
                                             '+5',
                                             'Apta para todo publico',
                                             1))
        update_atributo_clasificacion_pelicula(conn,
                                               'descripcion',
                                               ('Apta para todo publico', 2))

        # actualizar pelicula
        update_pelicula(conn, ('El señor de los anillos',
                               'Una pelicula de aventuras',
                               'Deben cuidar un anillo',
                               '185',
                               1,
                               1,
                               1))
        update_atributo_pelicula(conn, 'nombre', ('El señor de los anillos 2', 2))

        # actualizar descuento
        update_descuento(conn, ("Lunes", 0.5, 1))
        update_atributo_descuento(conn, "porcentaje", (0.5,  4))

        # actualizar usuario
        update_usuario(conn, ('Juan', 'Perez', 'juan_perez@gmail.com', '01010101', '2020-01-01', 'juan_perez', '123456abcd#', 'admin', 1))
        update_atributo_usuario(conn, "nombre", ("Pedrito", 2))

        # actualizar tarjeta
        update_tarjeta(conn, ('1234567890123456', 'Patagonia', 'Josecito', '2020-01-01', '123', 1, 1))
        update_atributo_tarjeta(conn, "numero", ('1234567890123457', 2))

        # actualizar sala
        update_sala(conn, (1, '2D', 100, 1))
        update_atributo_sala(conn, "formato", ("3D", 3))

        # actualizar butaca
        update_butaca(conn, ("B", 1, 'Si', 1, 1))
        update_atributo_butaca(conn, "fila", ("D", 2))

        # update sesion
        update_sesion(conn, ('2022-01-01', '00:00:00', 1, 5, 1))
        update_atributo_sesion(conn, "fecha", ('2022-01-01', 2))

        # update reserva
        update_reserva(conn, (1000, '2022-01-01', 1, 2, 3, 1, 2, 3))
        update_atributo_reserva(conn, "precio", (1000, 2))

        print("Valores actualizados")


if __name__ == '__main__':
    # main()
    pass
