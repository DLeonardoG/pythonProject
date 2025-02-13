from modulos.menus import *
from modulos.datos import *
from modulos.buscar import *
from tabulate import tabulate

def editar():
  while (True):
      try:
          match menuEditar():
            case "1":
                print("Editar Título")
                editarFuncion("titulo")
            case "2":
                print("Editar creador")
                editarFuncion("creador")
            case "3":
                print("Editar genero")
                editarFuncion("genero")
            case "4":
                print("Editar Valoración")
                editarFuncion("valoracion")
            case "5": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  


def editarFuncion(valorAEditar):
    elementoAEditar =  input("Ingrese el " + valorAEditar + " a editar: ")
    rutas = [RUTA_LIBROS, RUTA_MUSICA, RUTA_PELICULAS]
    for ruta in rutas:
        datos = cargarDatos(ruta) 
        dato = buscando(valorAEditar, datos, elementoAEditar)
        
        if dato:
            nuevoValor = input("Ingrese el nuevo " + valorAEditar + " : ")
            dato[valorAEditar] = nuevoValor
            print(datos)
            guardarDatos(datos, ruta)
            print("Guardado con exito...")
            return
    print("no se encontro")
    input("Enter para continuar... ")
    return

def buscando(valorAEditar, datos, elementoAEditar):
    for dato in datos:
        if dato.get(valorAEditar, "").lower() == elementoAEditar.lower():
            return dato
    return None

