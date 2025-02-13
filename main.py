from importaciones import *

def menu():
  while (True):
      try:
          match menuPrincipal():
            case "1": #añadir nuevo elemento
                añadir()
            case "2":#ver todos los elementos
                verTodos()
            case "3":#buscar elementos, ya sea por titulo, autoro genero
                buscar()
            case "4":#editar todo los elementos
                editar()
            case "5":#eliminar elementos
                eliminar()
            case "6":#ver elementos por categoria
                verPorCategoria()
            case "7":
                coleccion()
            case "8": #salir del programa
                print("Saliendo...")
                break
            case _:
                print("no es valido")
      
      except Exception as e:        
              print(f"Error: {e}. Selecciona una opción correcta.")
              input("Presiona Enter para continuar...")  

menu()



