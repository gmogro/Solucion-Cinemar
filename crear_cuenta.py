
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from pathlib import Path
from datetime import datetime
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from Clases.Usuario import Usuario
from BDD.creando_bdd import create_connection
from BDD.consulta_usuario import valid_user
from BDD.consulta_usuario import valid_email
from BDD.consulta_usuario import valid_dni

class CrearCuenta(Toplevel):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/crear_cuenta")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#FFFFFF")
        self.geometry("400x470")
        # Icono del programa
        self.iconbitmap(r'assets\cinemark.ico')
        # Titulo del programa
        self.title("Supermarket")
        self.create_widgets()

    def get_nombre(self):
        return self.entry_nombre.get()

    def get_apellido(self):
        return self.entry_apellido.get()

    def get_email(self):
        return self.entry_email.get()

    def get_dni(self):
        return self.entry_dni.get()

    def get_fecha_nacimiento(self):
        return self.entry_fecha_nacimiento.get()

    def get_username(self):
        return self.entry_username.get()

    def get_password(self):
        return self.entry_password.get()

    def get_repeat_password(self):
        return self.entry_repeat_password.get()

    def get_admin(self):
        if self.confirmar_admin():
            if self.entry_admin.get() == "SI":
                return "admin"
            else:
                return "cliente"

    def imprimir_datos(self):
        return f"{self.get_nombre()} {self.get_apellido()} {self.get_email()} {self.get_dni()} {self.get_fecha_nacimiento()} {self.get_username()} {self.get_password()} {self.get_repeat_password()} {self.get_admin()}"

    def confirmar_password(self):
        return self.get_password() == self.get_repeat_password()

    def confirmar_fecha(self):
        try:
            if datetime.strptime(self.get_fecha_nacimiento(), '%Y-%m-%d'):
                return True
        except ValueError:
            return False

    def confirmar_nombre_apellido(self):
        return self.get_nombre() != "" and self.get_apellido() != ""

    def confirmar_username(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        return not valid_user(conn, self.get_username()) or self.get_username() == ""

    def comprobar_dni(self):
        return len(self.get_dni()) == 8 and self.get_dni().isdigit()

    def confirmar_dni(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        return self.comprobar_dni() and not valid_dni(conn, self.get_dni())

    def comprobar_email(self):
        return "@" in self.get_email() and "." in self.get_email()

    def confirmar_email(self):
        database = r"Cinemark.db"
        # create a database connection
        conn = create_connection(database)
        return self.comprobar_email() and not valid_email(conn, self.get_email())

    def confirmar_admin(self):
        return self.entry_admin.get() == "SI" or self.entry_admin.get() == "NO"

    def comprobaciones(self):
        if self.confirmar_nombre_apellido():
            if self.confirmar_dni():
                if self.confirmar_email():
                    if self.confirmar_fecha():
                        if self.confirmar_username():
                            if self.confirmar_password():
                                if self.confirmar_admin():
                                    return True
                                else:
                                    messagebox.showerror("Error", "El campo de admin no es correcto")
                            else:
                                messagebox.showerror("Error", "Las contrase??as no coinciden")
                        else:
                            messagebox.showerror("Error", "El usuario ya existe")
                    else:
                        messagebox.showerror("Error", "La fecha no es correcta")
                else:
                    messagebox.showerror("Error", "El email ya existe o es incorrecto")
            else:
                messagebox.showerror("Error", "El DNI ya existe o es incorrecto")
        else:
            messagebox.showerror("Error", "El nombre y apellido no pueden estar vacios")

    def limpiar_entradas(self):
        self.entry_nombre.delete(0, 'end')
        self.entry_apellido.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_dni.delete(0, 'end')
        self.entry_fecha_nacimiento.delete(0, 'end')
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_repeat_password.delete(0, 'end')
        self.entry_admin.delete(0, 'end')

    def crear_usuario(self):
        if self.comprobaciones():
            database = r"Cinemark.db"
            # create a database connection
            conn = create_connection(database)
            usuario = Usuario(self.get_nombre(), self.get_apellido(), self.get_email(), self.get_dni(), self.get_fecha_nacimiento(), self.get_username(), self.get_password(), self.get_admin())
            usuario.insertar_usuario(conn)
            messagebox.showerror("Exito", "Usuario creado correctamente")
            self.limpiar_entradas()
        else:
            print("Ver comprobaciones")

    def create_widgets(self):
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=470,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            131.0,
            5.0,
            anchor="nw",
            text="Supermarket",
            fill="#11AC0E",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            5.0,
            35.0,
            anchor="nw",
            text="Crear Cuenta: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            17.0,
            71.0,
            anchor="nw",
            text="Nombre ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            17.0,
            388.0,
            anchor="nw",
            text="Admin: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            330.0,
            anchor="nw",
            text="Repite Contrase??a: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            17.0,
            71.0,
            anchor="nw",
            text="Nombre: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            297.0,
            anchor="nw",
            text="Contrase??a: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            238.0,
            anchor="nw",
            text="Nombre usuario:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            238.0,
            anchor="nw",
            text="Nombre usuario:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            203.0,
            anchor="nw",
            text="Fecha Nacimiento: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            17.0,
            137.0,
            anchor="nw",
            text="Email:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            15.0,
            170.0,
            anchor="nw",
            text="DNI: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            17.0,
            104.0,
            anchor="nw",
            text="Apellido: ",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        entry_image_nombre = PhotoImage(
            file = self.relative_to_assets("entry_nombre.png"))
        entry_bg_nombre = canvas.create_image(
            169.0,
            79.5,
            image=entry_image_nombre
        )
        self.entry_nombre = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_nombre.place(
            x=93.0,
            y=69.0,
            width=152.0,
            height=19.0
        )

        entry_image_apellido = PhotoImage(
            file = self.relative_to_assets("entry_apellido.png"))
        entry_bg_apellido = canvas.create_image(
            245.0,
            335.5,
            image=entry_image_apellido
        )
        self.entry_apellido = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_apellido.place(
            x=89.0,
            y=100.0,
            width=152.0,
            height=19.0
        )

        entry_image_email = PhotoImage(
            file = self.relative_to_assets("entry_email.png"))
        entry_bg_email = canvas.create_image(
            109.0,
            391.5,
            image=entry_image_email
        )
        self.entry_email = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_email.place(
            x=67.0,
            y=133.0,
            width=152.0,
            height=19.0
        )

        entry_image_dni = PhotoImage(
            file = self.relative_to_assets("entry_dni.png"))
        entry_bg_dni = canvas.create_image(
            195.0,
            303.5,
            image=entry_image_dni
        )
        self.entry_dni = Entry(
            self, 
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_dni.place(
            x=54.0,
            y=166.0,
            width=152.0,
            height=19.0
        )

        entry_image_fecha = PhotoImage(
            file = self.relative_to_assets("entry_fecha.png"))
        entry_bg_fecha = canvas.create_image(
            219.0,
            245.5,
            image=entry_image_fecha
        )
        self.entry_fecha_nacimiento = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_fecha_nacimiento.place(
            x=153.0,
            y=200.0,
            width=132.0,
            height=19.0
        )

        entry_image_username = PhotoImage(
            file = self.relative_to_assets("entry_username.png"))
        entry_bg_username = canvas.create_image(
            219.0,
            210.5,
            image=entry_image_username
        )
        self.entry_username = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_username.place(
            x=143.0,
            y=235.0,
            width=152.0,
            height=19.0
        )

        entry_image_password = PhotoImage(
            file = self.relative_to_assets("entry_password.png"))
        entry_bg_password = canvas.create_image(
            130.0,
            176.5,
            image=entry_image_password
        )
        self.entry_password = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_password.place(
            x=119.0,
            y=293.0,
            width=152.0,
            height=19.0
        )

        entry_image_repeat_password = PhotoImage(
            file = self.relative_to_assets("entry_repeat_password.png"))
        entry_bg_repeat_password = canvas.create_image(
            143.0,
            143.5,
            image=entry_image_password
        )
        self.entry_repeat_password = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_repeat_password.place(
            x=169.0,
            y=325.0,
            width=152.0,
            height=19.0
        )

        entry_image_admin = PhotoImage(
            file = self.relative_to_assets("entry_admin.png"))
        entry_bg_admin = canvas.create_image(
            165.0,
            110.5,
            image=entry_image_admin
        )
        self.entry_admin = Entry(
            self, 
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_admin.place(
            x=82.0,
            y=381.0,
            width=54.0,
            height=19.0
        )

        canvas.create_text(
            292.0,
            203.0,
            anchor="nw",
            text="(aaaa-mm-dd)",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        canvas.create_text(
            153.0,
            383.0,
            anchor="nw",
            text="(SI-NO)",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        button_image_confirmar = PhotoImage(
            file= self.relative_to_assets("button_confirmar.png"))
        button_confirmar = Button(
            self,
            image=button_image_confirmar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.crear_usuario(),
            relief="flat"
        )
        button_confirmar.place(
            x=163.0,
            y=425.0,
            width=111.0,
            height=29.0
        )

        button_image_salir = PhotoImage(
            file= self.relative_to_assets("button_salir.png"))
        button_salir = Button(
            self,
            image=button_image_salir,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_salir.place(
            x=7.0,
            y=431.0,
            width=35.0,
            height=35.0
        )

        canvas.create_text(
            17.0,
            260.0,
            anchor="nw",
            text="---------------------",
            fill="#000000",
            font=("Inter Bold", 25 * -1)
        )

        canvas.create_text(
            17.0,
            351.0,
            anchor="nw",
            text="---------------------",
            fill="#000000",
            font=("Inter Bold", 25 * -1)
        )
        self.resizable(False, False)
        self.mainloop()


if __name__ == "__main__":
    # app = CrearCuenta()
    pass
