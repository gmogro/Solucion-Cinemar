from BDD.insertando_datos_bdd import create_reserva
class Reserva:

    def __init__(self, precio, fecha, id_sesion, id_butaca, id_usuario, id_tarjeta, id_descuento, id_reserva=None):
        self.precio = precio
        self.fecha = fecha
        self.id_sesion = id_sesion
        self.id_butaca = id_butaca
        self.id_usuario = id_usuario
        self.id_tarjeta = id_tarjeta
        self.id_descuento = id_descuento
        self.id_reserva = id_reserva

    def to_list_complete(self):
        return [self.precio, self.fecha, self.id_sesion, self.id_butaca, self.id_usuario, self.id_tarjeta, self.id_descuento, self.id_reserva]

    def to_list_without_id(self):
        return [self.precio, self.fecha, self.id_sesion, self.id_butaca, self.id_usuario, self.id_tarjeta, self.id_descuento]

    def insertar_reserva(self, conn):
        create_reserva(conn, self.to_list_without_id())
        print("Reserva insertado correctamente")
