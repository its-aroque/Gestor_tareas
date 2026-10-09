
import tkinter as tk
from tkinter import ttk, messagebox
from tareas import GestorTareas

# Colores del proyecto
FONDO = "#F7F3EC"
VERDE = "#A8BBA3"
VERDE_OSCURO = "#626B5E"
BLANCO = "#FFFFFF"
ROSA = "#E8BFC3"
BEIGE = "#D6B99B"

# Gestor de tareas
gestor = GestorTareas()

# Ventana principal
app = tk.Tk()
app.title("Gestor de Tareas")
app.geometry("1100x700")
app.minsize(900, 600)
app.configure(bg=FONDO)

# Barra lateral
sidebar = tk.Frame(app, bg=VERDE, width=230)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="Cozy Planner",
    bg=VERDE,
    fg=BLANCO,
    font=("Segoe UI", 20, "bold")
).pack(pady=(40, 35))

# Contenido principal
contenido = tk.Frame(app, bg=FONDO)
contenido.pack(side="left", fill="both", expand=True, padx=35, pady=30)


def limpiar_contenido():
    for widget in contenido.winfo_children():
        widget.destroy()


def crear_titulo(texto, subtitulo):
    tk.Label(
        contenido,
        text=texto,
        bg=FONDO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 26, "bold")
    ).pack(anchor="w")

    tk.Label(
        contenido,
        text=subtitulo,
        bg=FONDO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=(5, 25))


def mostrar_inicio():
    limpiar_contenido()
    crear_titulo(
        "Mi espacio de estudio",
        "Organiza tus tareas, clases y metas a tu ritmo."
    )

    tarjeta = tk.Frame(contenido, bg=BLANCO, padx=25, pady=25)
    tarjeta.pack(fill="x")

    tk.Label(
        tarjeta,
        text="Bienvenida a Gestor de Tareas",
        bg=BLANCO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w")

    tk.Label(
        tarjeta,
        text="Selecciona Mis tareas para comenzar a organizarte.",
        bg=BLANCO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=(10, 0))


def nueva_tarea():
    ventana = tk.Toplevel(app)
    ventana.title("Nueva tarea")
    ventana.geometry("420x390")
    ventana.configure(bg=FONDO)
    ventana.transient(app)
    ventana.grab_set()

    tk.Label(
        ventana,
        text="Agregar nueva tarea",
        bg=FONDO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        ventana, text="Nombre de la tarea",
        bg=FONDO, fg=VERDE_OSCURO
    ).pack()

    entrada_titulo = tk.Entry(ventana, width=38)
    entrada_titulo.pack(pady=8)

    tk.Label(
        ventana, text="Asignatura",
        bg=FONDO, fg=VERDE_OSCURO
    ).pack()

    entrada_asignatura = tk.Entry(ventana, width=38)
    entrada_asignatura.pack(pady=8)

    tk.Label(
        ventana, text="Estado",
        bg=FONDO, fg=VERDE_OSCURO
    ).pack()

    estado = ttk.Combobox(
        ventana,
        values=["Por empezar", "En proceso", "Terminada"],
        state="readonly",
        width=35
    )
    estado.set("Por empezar")
    estado.pack(pady=8)

    def guardar():
        try:
            gestor.agregar_tarea(
                entrada_titulo.get(),
                entrada_asignatura.get(),
                estado.get()
            )
            ventana.destroy()
            mostrar_tareas()
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventana,
        text="Guardar tarea",
        command=guardar,
        bg=VERDE,
        fg=BLANCO,
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        padx=20,
        pady=10
    ).pack(pady=25)


def mostrar_tareas():
    limpiar_contenido()

    crear_titulo(
        "Mis tareas",
        "Organiza tus pendientes y celebra tus avances."
    )

    tk.Button(
        contenido,
        text="+ Nueva tarea",
        command=nueva_tarea,
        bg=VERDE,
        fg=BLANCO,
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        padx=18,
        pady=10
    ).pack(anchor="w", pady=(0, 20))

    tareas = gestor.obtener_tareas()

    if not tareas:
        tk.Label(
            contenido,
            text="Todavia no tienes tareas. Agrega tu primera tarea.",
            bg=FONDO,
            fg=VERDE_OSCURO,
            font=("Segoe UI", 12)
        ).pack(pady=30)
        return

    for tarea in tareas:
        tarjeta = tk.Frame(
            contenido,
            bg=BLANCO,
            padx=15,
            pady=12
        )
        tarjeta.pack(fill="x", pady=6)

        texto = (
            f"{tarea['titulo']}\n"
            f"Curso: {tarea['curso']}  |  "
            f"Estado: {tarea['estado']}"
        )

        tk.Label(
            tarjeta,
            text=texto,
            bg=BLANCO,
            fg=VERDE_OSCURO,
            justify="left",
            font=("Segoe UI", 11)
        ).pack(side="left")

        if not tarea["completada"]:
            tk.Button(
                tarjeta,
                text="Completar",
                bg=ROSA,
                relief="flat",
                command=lambda id=tarea["id"]: completar(id)
            ).pack(side="right")


def completar(id_tarea):
    gestor.completar_tarea(id_tarea)
    mostrar_tareas()


def mostrar_proximamente(seccion):
    limpiar_contenido()
    crear_titulo(
        seccion,
        "Esta seccion estara disponible proximamente."
    )


# Botones de navegacion
opciones = [
    ("Inicio", mostrar_inicio),
    ("Mis tareas", mostrar_tareas),
    ("Calendario", lambda: mostrar_proximamente("Calendario")),
    ("Horario", lambda: mostrar_proximamente("Horario")),
    ("Cursos", lambda: mostrar_proximamente("Cursos"))
]

for texto, funcion in opciones:
    tk.Button(
        sidebar,
        text=texto,
        command=funcion,
        bg=VERDE,
        fg=BLANCO,
        activebackground="#8FA68B",
        relief="flat",
        font=("Segoe UI", 12),
        anchor="w",
        padx=25,
        bd=0
    ).pack(fill="x", padx=10, pady=8)

# Mostrar pantalla inicial
mostrar_inicio()

# Ejecutar aplicacion
app.mainloop()
