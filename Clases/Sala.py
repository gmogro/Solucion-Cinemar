from BDD.insertando_datos_bdd import create_sala
class Sala:

    def __init__(self, numero, formato, capacidad, id_sala=None):
        self.numero = numero
        self.formato = formato
        self.capacidad = capacidad

    def to_list_complete(self):
        return [self.numero, self.formato, self.capacidad, self.id_sala]

    def to_list_without_id(self):
        return [self.numero, self.formato, self.capacidad]

    def insertar_sala(self, conn):
        create_sala(conn, self.to_list_without_id())
        print("Sala insertado correctamente")
