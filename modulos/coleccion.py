from modulos.menus import *
from modulos.datos import *
from tabulate import tabulate

def coleccionManejo(coleccion):
  while (True):
      try:
          match menuColeccion():
            case "1":
              print("Guardar la Colección Actual")
              print("--- Libros ---")
              coleccionParaGuardar(coleccion, "libros")
              print("--- Musica ---")
              coleccionParaGuardar(coleccion, "musica")
              print("--- Peliculas ---")
              coleccionParaGuardar(coleccion, "peliculas")
              print("¿Quieres guardarla?")
              print("1. sí")
              print("2. no")
              opc1 = input(' >>>')
              match opc1:
                  case "1":
                      guardarColeccion(coleccion, RUTA_LIBROS, "libros")
                      guardarColeccion(coleccion, RUTA_PELICULAS, "peliculas")
                      guardarColeccion(coleccion, RUTA_MUSICA, "musica")
                      guardarToda(RUTA_COLECCIONES,coleccion)
                      coleccion = {
                          "libros" : [],
                          "peliculas" : [],
                          "musica" : []
                        }
                      print("SE GUARDO TODO CORRECTAMENTE...")
                  case "2":
                      print("No se guardó la colección.")
                      return coleccion
                  case _:
                      print("Opción inválida.")
            case "2":
                print("Cargar una Colección Guardada")
                verLasColecciones(RUTA_COLECCIONES)
            case "3": 
                print("Regresar al Menú Principal...")
                return coleccion
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  


def coleccionParaGuardar(coleccion, nombre):
    if coleccion[nombre]:  # Verifica si la lista no está vacía
        print(tabulate(coleccion[nombre], headers="keys", tablefmt="fancy_grid", numalign="center", showindex="always"))
    else:
        print(f"No hay {nombre} para mostrar.")

def guardarColeccion(coleccion, ruta, nombreLista):
    datos = cargarDatos(ruta)
    for ele in coleccion[nombreLista]:
        datos.append(ele)
    guardarDatos(datos, ruta)

def guardarToda(ruta, coleccion):
    datos = cargarDatos(ruta)
    datos.append(coleccion)
    guardarDatos(datos, ruta)


def verLasColecciones(ruta):
    datos = cargarDatos(ruta)
    counter = 1
    for i in datos:
        print("----------------------------------------------------------------------------------------")
        print("Colección " + str(counter))
        print("libros")
        print(tabulate(i["libros"], headers="keys", tablefmt="grid", numalign="center", showindex="always"))
        print("peliculas")
        print(tabulate(i["peliculas"], headers="keys", tablefmt="grid", numalign="center", showindex="always"))
        print("musica")
        print(tabulate(i["musica"], headers="keys", tablefmt="grid", numalign="center", showindex="always"))
        counter += 1
        print("----------------------------------------------------------------------------------------")
        input("Enter para continuar... ")

