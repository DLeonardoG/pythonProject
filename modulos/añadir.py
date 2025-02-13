from modulos.menus import *

def añadir():
  while (True):
      try:
          match menuAñadir():
            case "1":
              print("Libro")
            case "2":
                print("Película")
            case "3":
                print("Música")
            case "4": 
                print("Regresar al Menú Principal...")
                break
            case _:
                print("Ingrese una funcion valida")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  




