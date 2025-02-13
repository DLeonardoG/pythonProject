import json

def cargarDatos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardarDatos(datos, archivo):
    datos = dict(datos)
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    

#Constantes
RUTA_MUSICA ="datos\musica.json"
RUTA_LIBROS ="datos\libros.json"
RUTA_PELICULAS ="datos\peliculas.json"
RUTA_COLECCIONES ="datos\colecciones.json"