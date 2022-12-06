from BDD import consulta_producto
from BDD import insertando_datos_bdd
from BDD import actualizando_bdd
from BDD import eliminando_bdd

class Tarjeta_Credito:
    
    def __init__(self, numero, banco, titular, fecha_caducidad, codigo_seguridad, id_usuario, id_tarjeta=0):
        self.numero = numero
        self.banco = banco
        self.titular = titular
        self.fecha_caducidad = fecha_caducidad
        self.codigo_seguridad = codigo_seguridad
        self.id_usuario = id_usuario
        self.id_tarjeta = id_tarjeta
        
    def __str__(self):
        return "Tarjeta: {}, {}, {}, {}, {}, {}".format(self.numero, self.banco, self.titular, self.fecha_caducidad, self.codigo_seguridad, self.id_usuario)
    
    def get_numero_tarjeta(self):
        return self.numero
    
    def get_banco(self):
        return self.banco
    
    def get_titular(self):
        return self.titular
    
    def get_fecha_caducidad(self):
        return self.fecha_caducidad
    
    def get_codigo_seguridad(self):
        return self.codigo_seguridad
    
    def get_id_usuario(self):
        return self.id_usuario
    
    def get_id_tarjeta(self):
        return self.id_tarjeta
    
    def set_numero_tarjeta(self, numero):
        self.numero = numero
    
    def set_banco(self, banco):
        self.banco = banco
    
    def set_titular(self, titular):
        self.titular = titular
    
    def set_fecha_caducidad(self):
        return self.fecha_caducidad
    
    def set_codigo_seguridad(self):
        return self.codigo_seguridad
    
    def set_id_usuario(self):
        return self.id_usuario
    
    def set_id_tarjeta(self):
        return self.id_tarjeta
    
    def to_list_complete(self):
        return [self.numero, self.banco, self.titular, self.fecha_caducidad, self.codigo_seguridad, self.id_usuario, self.id_tarjeta]
    
    def to_list_without_id(self):
        return [self.numero, self.banco, self.titular, self.fecha_caducidad, self.codigo_seguridad, self.id_usuario]
    
    def insertar_tarjeta(self, conn):
        insertando_datos_bdd.create_tarjeta_credito(
            conn, self.to_list_without_id())
        print("Valor insertado correctamente")
        
    def modificar_tarjeta(self, conn):
        actualizando_bdd.update_tarjeta_credito(conn, self.to_list_complete())
        print("Valor modificado correctamente")
        
    def modificar_atributo_tarjeta(self, conn, atributo, valor):
        actualizando_bdd.update_atributo_tarjeta_credito(conn, atributo, (valor, self.id_tarjeta))
        print("Valor modificado correctamente")
        
    def eliminar_tarjeta(self, conn):
        eliminando_bdd.delete_row_table_by_id(conn, "tarjeta_credito", self.id_tarjeta)
        print("Valor eliminado correctamente")