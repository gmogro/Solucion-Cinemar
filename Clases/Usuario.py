
from BDD import consulta_usuario
from BDD.insertando_datos_bdd import create_usuario
from BDD import actualizando_bdd
from BDD import eliminando_bdd

class Usuario:

    def __init__(self, nombre, apellido, email, dni, fecha_nacimiento, username, password, tipo, id_usuario = None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.username = username
        self.password = password
        self.tipo = tipo
        self.id_usuario = id_usuario

    def __str__(self):
        return "Usuario: {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.nombre, self.apellido, self.dni, self.email, self.fecha_nacimiento, self.username, self.password, self.tipo, self.id_usuario)

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni

    def get_email(self):
        return self.email

    def get_id_usuario(self):
        return self.id_usuario

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_tipo(self):
        return self.tipo

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_tipo(self, tipo):
        self.tipo = tipo

    def to_list_complete(self):
        return [self.nombre, self.apellido, self.dni, self.email, self.fecha_nacimiento, self.username, self.password, self.tipo, self.id_usuario]

    def to_list_without_id(self):
        return [self.nombre, self.apellido, self.dni, self.email, self.fecha_nacimiento, self.username, self.password, self.tipo]

    def insertar_usuario(self, conn):
        create_usuario(conn, self.to_list_without_id())
        print("Usuario insertado correctamente")

    def modificar_usuario(self, conn):
        actualizando_bdd.update_usuario(conn, self.to_list_complete())
        print("Usuario modificado correctamente")

    def modificar_atributo_usuario(self, conn, atributo, valor):
        actualizando_bdd.update_atributo_usuario(conn, atributo, (valor, self.id_usuario))
        print("Usuario modificado correctamente")

    def eliminar_usuario(self, conn):
        eliminando_bdd.delete_row_table_by_id(conn, 'usuario', self.id_usuario)
        print("Usuario eliminado correctamente")

