# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from BDD.creando_bdd import create_connection
from BDD.actualizando_bdd import update_sala


def select_sala(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM sala")
    rows = cur.fetchall()
    conn.close()
    return rows

def select_sala_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM sala WHERE id_sala = ?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows


class AdministracionModificarSala(Toplevel):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / \
        Path("./assets/administracion_modificar_sala")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#FFFFFF")
        self.geometry("428x360")
        # Icono del programa
        self.iconbitmap(r'assets\cinemark.ico')
        # Titulo del programa
        self.title("Cinemark")
        self.create_widgets()

    def get_coloca_id(self):
        return self.entry_coloca_id.get()

    def get_formato(self):
        return self.entry_formato.get()

    def get_capacidad(self):
        return self.entry_capacidad.get()

    def set_formato(self, formato):
        self.entry_formato.delete(0, "end")
        self.entry_formato.insert(0, formato)

    def set_capacidad(self, capacidad):
        self.entry_capacidad.delete(0, "end")
        self.entry_capacidad.insert(0, capacidad)

    def limpiar_busqueda(self):
        self.entry_resultado_busqueda.delete(1.0, "end")

    def limpiar_entradas(self):
        self.entry_coloca_id.delete(0, "end")
        self.entry_formato.delete(0, "end")
        self.entry_capacidad.delete(0, "end")

    def cargar_datos_salas(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        id = self.get_coloca_id()
        resultados = select_sala_by_id(conn, id)
        self.set_formato(resultados[0][2])
        self.set_capacidad(resultados[0][3])

    def mostrar_salas(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        salas = select_sala(conn)
        for sala in salas:
            self.entry_resultado_busqueda.insert(
                "insert", f" {sala[0]} -- {sala[1]} --  {sala[2]}  -- {sala[3]}\n")

    def actualizar_sala(self):
        database = r"Cinemark.db"
        conn = create_connection(database)
        cur = conn.cursor()
        update_sala(conn, (self.get_coloca_id(), self.get_formato(), self.get_capacidad(), self.get_coloca_id()))
        self.limpiar_busqueda()
        self.mostrar_salas()

    def create_widgets(self):
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 499,
            width = 428,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            131.0,
            5.0,
            anchor="nw",
            text="Cinemark",
            fill="#11AC0E",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            6.0,
            198.0,
            anchor="nw",
            text="Modificar Sala: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )


        canvas.create_text(
            16.0,
            268.0,
            anchor="nw",
            text="Capacidad: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            18.0,
            234.0,
            anchor="nw",
            text="Formato: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        entry_image_1 = PhotoImage(
            file = self.relative_to_assets("entry_nombre_producto.png"))
        entry_bg_1 = canvas.create_image(
            170.0,
            242.5,
            image=entry_image_1
        )
        self.entry_formato = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_formato.place(
            x=94.0,
            y=232.0,
            width=152.0,
            height=19.0
        )
        # self.entry_nombre_producto.insert(0, "nombre_producto")

        entry_image_3 = PhotoImage(
            file = self.relative_to_assets("entry_coloca_id.png"))
        entry_bg_3 = canvas.create_image(
            318.0,
            116.5,
            image=entry_image_3
        )
        self.entry_coloca_id = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_coloca_id.place(
            x=242.0,
            y=106.0,
            width=152.0,
            height=19.0
        )
        # self.entry_coloca_id.insert(0, "coloca_id")

        entry_image_5 = PhotoImage(
            file = self.relative_to_assets("entry_stock_producto.png"))
        entry_bg_5 = canvas.create_image(
            176.0,
            272.5,
            image=entry_image_5
        )
        self.entry_capacidad = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_capacidad.place(
            x=100.0,
            y=262.0,
            width=152.0,
            height=19.0
        )
        # self.entry_stock_producto.insert(0, "stock_producto")


        button_image_1 = PhotoImage(
            file = self.relative_to_assets("button_confirmar.png"))
        button_confirmar = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.actualizar_sala(),
            relief="flat"
        )
        button_confirmar.place(
            x=164.0,
            y=310.0,
            width=111.0,
            height=29.0
        )

        button_image_2 = PhotoImage(
            file = self.relative_to_assets("button_cargar.png"))
        button_cargar = Button(
            self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_datos_salas(),
            relief="flat"
        )
        button_cargar.place(
            x=262.0,
            y=136.0,
            width=111.0,
            height=29.0
        )

        button_image_3 = PhotoImage(
            file = self.relative_to_assets("button_salir.png"))
        button_salir = Button(
            self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_salir.place(
            x=13.0,
            y=320.0,
            width=35.0,
            height=35.0
        )
        # Button Limpiar
        button_buscar = Button(
            self,
            text="Limpiar",
            command=lambda: self.limpiar_entradas(),
            relief="flat"
        )
        button_buscar.place(
            x=300.0,
            y=250.0,
            width=50.00,
            height=29.0
        )

        canvas.create_text(
            18.0,
            35.0,
            anchor="nw",
            text="  Id - Numero - Formato - Capacidad",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            266.0,
            79.0,
            anchor="nw",
            text="Coloca su ID:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        entry_image_9 = PhotoImage(
            file = self.relative_to_assets("entry_resultado_busqueda.png"))
        entry_bg_9 = canvas.create_image(
            113.5,
            127.0,
            image=entry_image_9
        )
        self.entry_resultado_busqueda = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_resultado_busqueda.place(
            x=13.0,
            y=66.0,
            width=201.0,
            height=120.0
        )
        # self.entry_resultado_busqueda.insert("insert", "resultados_busqueda")

        self.mostrar_salas()
        self.resizable(False, False)
        self.mainloop()


if __name__ == "__main__":
    # app = AdministracionModificarSala()
    pass
