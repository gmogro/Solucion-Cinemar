# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from BDD.creando_bdd import create_connection
from BDD.eliminando_bdd import delete_row_table_by_id


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


class AdministracionEliminarSala(Toplevel):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / \
        Path("./assets/administracion_eliminar_sala")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#FFFFFF")
        self.geometry("428x250")
        # Icono del programa
        self.iconbitmap(r'assets\cinemark.ico')
        # Titulo del programa
        self.title("Cinemark")
        self.create_widgets()

    def get_coloca_id(self):
        return self.entry_coloca_id.get()


    def limpiar_busqueda(self):
        self.entry_resultado_busqueda.delete(1.0, "end")

    def eliminar_datos_salas(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        cur = conn.cursor()
        delete_row_table_by_id(conn, "sala", self.get_coloca_id())
        self.limpiar_busqueda()
        self.entry_coloca_id.delete(0, "end")
        self.mostrar_salas()

    def mostrar_salas(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        salas = select_sala(conn)
        for sala in salas:
            self.entry_resultado_busqueda.insert(
                "insert", f" {sala[0]} -- {sala[1]} --  {sala[2]}  -- {sala[3]}\n")

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

        button_image_2 = PhotoImage(
            file = self.relative_to_assets("button_eliminar.png"))
        button_cargar = Button(
            self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.eliminar_datos_salas(),
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
            y=205.0,
            width=35.0,
            height=35.0
        )

        canvas.create_text(
            10.0,
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
    # app = AdministracionEliminarSala()
    pass
