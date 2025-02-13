from modulos.menus import *
from modulos.datos import *
from tabulate import tabulate

def buscar():
  while (True):
      try:
          match menuBuscar():
            case "1":
                print("Buscar por Título")
                buscarFuncion ("titulo")
            case "2":
                print("Buscar por creador")
                buscarFuncion ("creador")
            case "3":
                print("Buscar por genero")
                buscarFuncion ("genero")
            case "4": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




def buscarFuncion (valorABuscar):
    elementoABuscar =  input("Ingrese el " + valorABuscar + " a buscar: ")
    results = []
    rutas = [RUTA_LIBROS, RUTA_MUSICA, RUTA_PELICULAS]
    for ruta in rutas:
        datos = cargarDatos(ruta) 
        dato = buscando(valorABuscar, datos, elementoABuscar)
        if dato:
            results.append([dato[valorABuscar], dato["creador"], dato["genero"], dato["valoracion"]])

    print("Resultados: ")
    print(tabulate(results, headers=["titulo", "creador", "genero", "valoracion"], tablefmt="grid", numalign="center", showindex="always"))
    input("Enter para continuar... ")

def buscando(valorABuscar, datos, elementoABuscar):
    for dato in datos:
        if dato.get(valorABuscar, "").lower() == elementoABuscar.lower():
            return dato
    return None
