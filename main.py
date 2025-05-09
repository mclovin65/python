from programas.suma import sumar
from programas.restas import restar
from programas.multipllicaciones import multiplicar
from vistas.lineas import menu, lineas
from datetime import datetime
import threading

def mostrar_tiempo():
    while True:
        print(f"Tiempo actual: {datetime.now().strftime('%H:%M:%S')}", end="\r")


threading.Thread(target=mostrar_tiempo, daemon=True).start()

programa = True
while programa:
    lineas(40)
    menu()
    lineas(40)
    respuesta = int(input("|[?] "))
    if respuesta == 1:
        sumar()
    elif respuesta == 2:
        restar()
    elif respuesta == 3:
        multiplicar()
    elif respuesta == 4:
        print("Saliendo del programa...")
        programa = False