from modulos.menus import *

def eliminar():
  while (True):
      try:
          match menuEliminar():
            case "1":
              print("Eliminar por Título")
            case "2":
                print("Eliminar por Identificador Único")
            case "3": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




