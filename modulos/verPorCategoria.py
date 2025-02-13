from modulos.menus import *
from modulos.datos import *
from tabulate import tabulate


def verPorCategoria():
  while (True):
      try:
          match menuVerPorCategoria():
            case "1":
              print("--- Libros ---")
              verPorGenero(RUTA_LIBROS)
            case "2":
              print("--- Pelicula ---")
              verPorGenero(RUTA_PELICULAS)
            case "3":
              print("--- Musica ---")
              verPorGenero(RUTA_MUSICA)
            case "4": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  


def verPorGenero (ruta):
    while True:
        datos = cargarDatos(ruta) 
        genero = input("Ingrese el genero(drama, comedia...): ").strip().lower()
        elementos = list(filter(lambda elemento: elemento.get("genero", "").lower() == genero, datos))
        if elementos:
            print(tabulate(elementos, headers="keys", tablefmt="heavy_grid", numalign="center"))
        else:
            print("No se encontro ninguna coincidencia.")
        if input("¿Desea buscar más elementos? (s/n): ").strip().lower() == "n":
            break




