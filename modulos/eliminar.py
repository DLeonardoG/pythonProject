from modulos.menus import *
from modulos.datos import *

def eliminar():
  while (True):
      try:
          match menuEliminar():
            case "1":
                print("Eliminar por Título")
                eliminarFuncion("titulo")
            case "2":
                print("Eliminar por Identificador Único")
                eliminarFuncion("id")
            case "3": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  


def eliminarFuncion(valorAEliminar):
    elementoAEliminar = input("Ingrese el " + valorAEliminar + " a eliminar: ")
    rutas = [RUTA_LIBROS, RUTA_MUSICA, RUTA_PELICULAS]
    
    for ruta in rutas:
        datos = cargarDatos(ruta) 
        dato = buscando(valorAEliminar, datos, elementoAEliminar)
        
        if dato:
            datos.remove(dato) 
            guardarDatos(datos, ruta)
            print("Elemento eliminado con éxito...")
            input("Enter para continuar... ")
            return
    
    print("No se encontró el elemento a eliminar.")
    input("Enter para continuar... ")
    return

def buscando(valorAEliminar, datos, elementoAEliminar):
    for dato in datos:
        if dato.get(valorAEliminar, "").lower() == elementoAEliminar.lower():
            return dato
    return None
