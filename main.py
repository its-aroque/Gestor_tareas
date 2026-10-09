
import tkinter as tk
from tkinter import ttk, messagebox
from tareas import GestorTareas
import calendar
from datetime import date

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

    
def mostrar_calendario():
    limpiar_contenido()
    crear_titulo("Calendario", "Organiza tus dias de estudio.")

    hoy = date.today()
    mostrar_mes(hoy.year, hoy.month)


def mostrar_mes(anio, mes):
    limpiar_contenido()
    crear_titulo("Calendario", "Consulta tus fechas importantes.")

    encabezado = tk.Frame(contenido, bg=FONDO)
    encabezado.pack(pady=10)

    def anterior():
        nuevo_mes = mes - 1
        nuevo_anio = anio

        if nuevo_mes == 0:
            nuevo_mes = 12
            nuevo_anio -= 1

        mostrar_mes(nuevo_anio, nuevo_mes)

    def siguiente():
        nuevo_mes = mes + 1
        nuevo_anio = anio

        if nuevo_mes == 13:
            nuevo_mes = 1
            nuevo_anio += 1

        mostrar_mes(nuevo_anio, nuevo_mes)

    tk.Button(
        encabezado, text="<",
        command=anterior,
        bg=VERDE, fg=BLANCO,
        width=4
    ).pack(side="left", padx=15)

    nombre_mes = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ][mes - 1]

    tk.Label(
        encabezado,
        text=f"{nombre_mes} {anio}",
        bg=FONDO,
        fg=VERDE_OSCURO,
        font=("Segoe UI", 18, "bold")
    ).pack(side="left", padx=15)

    tk.Button(
        encabezado, text=">",
        command=siguiente,
        bg=VERDE, fg=BLANCO,
        width=4
    ).pack(side="left", padx=15)

    tabla = tk.Frame(contenido, bg=BLANCO, padx=15, pady=15)
    tabla.pack(pady=20)

    dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    for columna, dia in enumerate(dias):
        tk.Label(
            tabla,
            text=dia,
            bg=VERDE,
            fg=BLANCO,
            width=8,
            pady=10
        ).grid(row=0, column=columna, padx=2, pady=2)

    semanas = calendar.monthcalendar(anio, mes)

    for fila, semana in enumerate(semanas, start=1):
        for columna, dia in enumerate(semana):
            texto = str(dia) if dia != 0 else ""

            color = BLANCO
            if (
                dia == date.today().day
                and mes == date.today().month
                and anio == date.today().year
            ):
                color = ROSA

            tk.Label(
                tabla,
                text=texto,
                bg=color,
                fg=VERDE_OSCURO,
                width=8,
                height=3,
                relief="solid",
                borderwidth=1
            ).grid(row=fila, column=columna, padx=2, pady=2)



# Botones de navegacion
opciones = [
    ("Inicio", mostrar_inicio),
    ("Mis tareas", mostrar_tareas),
    ("Calendario", mostrar_calendario)
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
