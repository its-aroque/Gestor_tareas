
import tkinter as tk
from tkinter import ttk

# Colores del proyecto
FONDO = "#F7F3EC"
VERDE = "#A8BBA3"
TEXTO = "#626B5E"
BLANCO = "#FFFFFF"

# Ventana principal
app = tk.Tk()
app.title("Cozy Study Planner")
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

# Opciones del menu
opciones = ["Inicio", "Mis tareas", "Calendario", "Horario", "Cursos"]

for opcion in opciones:
    tk.Button(
        sidebar,
        text=opcion,
        bg=VERDE,
        fg=BLANCO,
        activebackground="#8FA68B",
        relief="flat",
        font=("Segoe UI", 12),
        anchor="w",
        padx=25,
        bd=0
    ).pack(fill="x", padx=10, pady=8)

# Contenido principal
contenido = tk.Frame(app, bg=FONDO)
contenido.pack(side="left", fill="both", expand=True, padx=40, pady=40)

tk.Label(
    contenido,
    text="Mi espacio de estudio",
    bg=FONDO,
    fg=TEXTO,
    font=("Segoe UI", 28, "bold")
).pack(anchor="w")

tk.Label(
    contenido,
    text="Organiza tus tareas, clases y metas a tu ritmo.",
    bg=FONDO,
    fg=TEXTO,
    font=("Segoe UI", 12)
).pack(anchor="w", pady=(10, 30))

# Tarjeta de bienvenida
tarjeta = tk.Frame(contenido, bg=BLANCO, padx=25, pady=25)
tarjeta.pack(fill="x")

tk.Label(
    tarjeta,
    text="Bienvenida a tu planner",
    bg=BLANCO,
    fg=TEXTO,
    font=("Segoe UI", 18, "bold")
).pack(anchor="w")

tk.Label(
    tarjeta,
    text="Aqui podras organizar tus tareas y visualizar tu progreso.",
    bg=BLANCO,
    fg=TEXTO,
    font=("Segoe UI", 11)
).pack(anchor="w", pady=(10, 0))

# Iniciar aplicacion
app.mainloop()
