from modulos.menus import *
from modulos.datos import *
from tabulate import tabulate

def verTodos():
  while (True):
      try:
          match menuVerTodos():
            case "1":
                print("--- Libros ---")
                verTodosFuncion(RUTA_LIBROS)
            case "2":
                print("--- Peliculas ---")
                verTodosFuncion(RUTA_PELICULAS)
            case "3":
                print("--- Musica ---")
                verTodosFuncion(RUTA_MUSICA)
            case "4": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  

def verTodosFuncion(ruta):
    datos = cargarDatos(ruta)
    datosImprimir = []
    for elemento in datos:
        datosImprimir.append(elemento)
    print(tabulate(datosImprimir, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("Enter para continuar...")
