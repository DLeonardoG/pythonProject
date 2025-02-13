from modulos.menus import *
from modulos.datos import *

def añadir(coleccion):
  while (True):
      try:
          match menuAñadir():
            case "1":
                print("Libro")
                coleccion = añadirFuncion(coleccion, "libros", "libro")
            case "2":
                print("Pelicula")
                coleccion = añadirFuncion(coleccion, "peliculas", "pelicula")
            case "3":
                print("Musica")
                coleccion = añadirFuncion(coleccion, "musica", "cancion")
            case "4": 
                print("Regresar al Menú Principal...")
                return coleccion
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  

def añadirFuncion(coleccion, nombreLista, elemento): #agregar cualquier cosa
        nuevoElemento = {
            "id" : verificaridUnico(),
            "titulo" : input("titulo de " + elemento + ": "),
            "creador" : input("creador de " + elemento + ": "),
            "genero" : input("genero de " + elemento + ": "),
            "valoracion" : validacionValida()
        }
        coleccion[nombreLista].append(nuevoElemento)
        print("Se añadio satisfactoriamente.")
        return coleccion

def verificaridUnico():
    while True:
        idIngresado = input("Ingrese un id unico de 5 caracteres: ").strip()
        if len(idIngresado) != 5:
            print("El id debe tener exactamente 5 caracteres. Intente nuevamente.")
            continue
        rutas = [RUTA_LIBROS, RUTA_MUSICA, RUTA_PELICULAS]
        idExistente = False
        for ruta in rutas:
            datos = cargarDatos(ruta)
            if buscandoPorid(idIngresado, datos):
                idExistente = True
                break
        if idExistente:
            print("El id ya existe. Intente con otro id.")
        else:
            print("El id es válido y único.")
            return idIngresado
def buscandoPorid(idBuscar, datos):
    for dato in datos:
        if dato.get("id", "").lower() == idBuscar.lower():
            return dato
    return None

def validacionValida():
    while True:
        valorIngresado = input("Ingrese la validacion entre 1 y 5: ").strip()        
        if valorIngresado.isdigit(): 
            valorNumerico = int(valorIngresado)
            if 1 <= valorNumerico <= 5:
                return valorIngresado 
            else:
                print("El valor debe estar entre 1 y 5. Intente nuevamente.")
        else:
            print("Entrada inválida. Debe ingresar un número. Intente nuevamente.")
