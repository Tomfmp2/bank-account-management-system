import os
def limpiar():
    # Limpia la consola dependiendo del sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')


def precionar_continuar():
    # entrada para que el usuario pueda leer mensajes antes de ser limpiados por la siguiente seccion
    input('\nPresione cualquier tecla para continuar..')
