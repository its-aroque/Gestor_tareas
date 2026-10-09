
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, curso, estado="Por empezar"):
        if not titulo.strip():
            raise ValueError("El titulo de la tarea no puede estar vacio")

        tarea = {
            "id": len(self.tareas) + 1,
            "titulo": titulo.strip(),
            "curso": curso,
            "estado": estado,
            "completada": False
        }

        self.tareas.append(tarea)
        return tarea

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                tarea["estado"] = "Terminada"
                return True

        return False
