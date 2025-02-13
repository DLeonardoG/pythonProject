from modulos.menus import *

def coleccion():
  while (True):
      try:
          match menuColeccion():
            case "1":
              print("Guardar la Colección Actual")
            case "2":
                print("Cargar una Colección Guardada")
            case "3": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




