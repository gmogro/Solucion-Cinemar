
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import RIGHT, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Scrollbar
from BDD.creando_bdd import create_connection
from BDD.consulta_usuario import select_usuario_by_id


def select_reserva(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva")

    rows = cur.fetchall()

    return rows


class AdministracionVerReservas(Toplevel):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / \
        Path("./assets/administracion_ver_reserva")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#FFFFFF")
        self.geometry("620x357")
        # Icono del programa
        self.iconbitmap(r'assets\cinemark.ico')
        # Titulo del programa
        self.title("Cinemark")
        self.create_widgets()

    def mostrar_reserva(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        reservas = select_reserva(conn)
        for reserva in reservas:
            usuario = select_usuario_by_id(conn, reserva[5])[0][1] + " " + select_usuario_by_id(conn, reserva[5])[0][2]
            self.text_reservas.insert(
                "insert", f"  ${reserva[1]} --  {reserva[2]}  --  {reserva[3]}    --     {reserva[4]}   --  {usuario} \n")

    def create_widgets(self):
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 357,
            width = 621,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            250.0,
            5.0,
            anchor="nw",
            text="Cinemark",
            fill="#11AC0E",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            220.0,
            35.0,
            anchor="nw",
            text="Reservas de Usuarios",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        button_image_salir = PhotoImage(
            file = self.relative_to_assets("button_salir.png"))
        button_salir = Button(
            self,
            image = button_image_salir,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_salir.place(
            x=9.0,
            y=314.0,
            width=35.0,
            height=35.0
        )

        entry_image_usuarios = PhotoImage(
            file = self.relative_to_assets("entry_usuarios.png"))
        entry_bg_usuarios = canvas.create_image(
            209.0,
            195.0,
            image=entry_image_usuarios
        )

        self.text_reservas = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.text_reservas.place(
            x=5.0,
            y=83.0,
            width=600.0,
            height=222.0
        )
        self.mostrar_reserva()

        canvas.create_text(
            5.0,
            59.0,
            anchor="nw",
            text="    Precio    --      Fecha      --    Sesion    --    Butaca     --  Usuario",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.resizable(False, False)
        self.mainloop()


if __name__ == "__main__":
    # app = AdministracionVerReservas()
    pass
