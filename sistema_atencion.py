"""
Sistema de atención - Ventanilla de Servicios Escolares
Estructura de datos: Fila (cola) implementada con nodos enlazados.
Principio FIFO: primeras entradas - primeras salidas.
"""


class Estudiante:
    """Guarda los datos de un estudiante."""

    def __init__(self, matricula, nombre, carrera, tramite):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.tramite = tramite

    def __str__(self):
        return (f"Matrícula: {self.matricula} | Nombre: {self.nombre} | "
                f"Carrera: {self.carrera} | Trámite: {self.tramite}")


class Nodo:
    """Cada nodo contiene un estudiante y la referencia al siguiente nodo."""

    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None


class FilaAtencion:
    """Fila (cola) FIFO: se agrega por el final y se atiende por el frente."""

    def __init__(self):
        self.frente = None   # primer estudiante (el que se atiende)
        self.final = None    # último estudiante (donde se forma el nuevo)
        self.tamanio = 0

    # f) Avisar si la fila está vacía
    def esta_vacia(self):
        return self.frente is None

    def alerta_fila_vacia(self):
        print("\n" + "!" * 50)
        print("  ALERTA: La fila está vacía. No hay estudiantes esperando.")
        print("!" * 50)

    # a) Agregar un estudiante a la fila (encolar)
    def agregar(self, estudiante):
        nuevo = Nodo(estudiante)
        if self.esta_vacia():
            self.frente = nuevo
        else:
            self.final.siguiente = nuevo
        self.final = nuevo
        self.tamanio += 1
        print(f"\n{estudiante.nombre} se formó en la fila. Posición: {self.tamanio}")

    # b) Atender al estudiante que se encuentra al frente (desencolar)
    def atender(self):
        if self.esta_vacia():
            self.alerta_fila_vacia()
            return None
        atendido = self.frente.estudiante
        self.frente = self.frente.siguiente
        if self.frente is None:      # si ya no queda nadie, el final también queda vacío
            self.final = None
        self.tamanio -= 1
        print("\nAtendiendo a:")
        print("  " + str(atendido))
        if self.esta_vacia():
            self.alerta_fila_vacia()
        return atendido

    # c) Consultar quién es el siguiente estudiante
    def consultar_siguiente(self):
        if self.esta_vacia():
            self.alerta_fila_vacia()
            return None
        print("\nSiguiente estudiante en ser atendido:")
        print("  " + str(self.frente.estudiante))
        return self.frente.estudiante

    # d) Mostrar todos los estudiantes que esperan
    def mostrar(self):
        if self.esta_vacia():
            self.alerta_fila_vacia()
            return
        print("\nEstudiantes en espera (del frente al final):")
        actual = self.frente
        posicion = 1
        while actual is not None:
            print(f"  {posicion}. {actual.estudiante}")
            actual = actual.siguiente
            posicion += 1

    # e) Determinar cuántos estudiantes están esperando
    def cantidad(self):
        return self.tamanio


def pedir_texto(mensaje):
    """Pide un dato y no permite dejarlo vacío."""
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("  Este dato es obligatorio.")


def menu():
    fila = FilaAtencion()

    while True:
        print("\n" + "=" * 50)
        print("   VENTANILLA DE SERVICIOS ESCOLARES")
        print("=" * 50)
        print("1. Agregar estudiante a la fila")
        print("2. Atender al estudiante del frente")
        print("3. Consultar siguiente estudiante")
        print("4. Mostrar estudiantes en espera")
        print("5. Cantidad de estudiantes esperando")
        print("6. Verificar si la fila está vacía")
        print("7. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("\n--- Datos del estudiante ---")
            matricula = pedir_texto("Matrícula: ")
            nombre = pedir_texto("Nombre: ")
            carrera = pedir_texto("Carrera: ")
            tramite = pedir_texto("Tipo de trámite: ")
            fila.agregar(Estudiante(matricula, nombre, carrera, tramite))

        elif opcion == "2":
            fila.atender()

        elif opcion == "3":
            fila.consultar_siguiente()

        elif opcion == "4":
            fila.mostrar()

        elif opcion == "5":
            print(f"\nEstudiantes esperando: {fila.cantidad()}")

        elif opcion == "6":
            if fila.esta_vacia():
                fila.alerta_fila_vacia()
            else:
                print(f"\nLa fila NO está vacía. Hay {fila.cantidad()} estudiante(s) esperando.")

        elif opcion == "7":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
