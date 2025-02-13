from modulos.menus import *

def editar():
  while (True):
      try:
          match menuEditar():
            case "1":
              print("Editar Título")
            case "2":
                print(" Editar Autor/Director/Artista")
            case "3":
                print("Editar Género")
            case "4":
                print("Editar Valoración")
            case "5": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




