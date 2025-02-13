import json

def cargarDatos(ruta):
    datos = {}
    with open(ruta,"r") as file:
        datos=json.load(file)
    return datos

def guardarDatos(datos, ruta):
    diccionario=json.dumps(datos, indent=4)
    file=open(ruta,"w")
    file.write(diccionario)
    file.close()
    

#Constantes
RUTA_MUSICA ="datos\musica.json"
RUTA_LIBROS ="datos\libros.json"
RUTA_PELICULAS ="datos\peliculas.json"
RUTA_COLECCIONES ="datos\colecciones.json"