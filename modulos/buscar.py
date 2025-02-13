from modulos.menus import *

def buscar():
  while (True):
      try:
          match menuBuscar():
            case "1":
              print("Buscar por Título")
            case "2":
                print("Buscar por Autor/Director/Artista")
            case "3":
                print("Buscar por Género")
            case "4": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




