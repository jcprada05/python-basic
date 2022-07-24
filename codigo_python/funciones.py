# Declaración de Función
def imprimir_mensaje():
  print("Mensaje especial: ")
  print("¡Estoy aprendiendo a usar funciones!")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

# Repitiendo Lógica
opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
  print("Hola")
  print("Cómo estás")
  print("Elegiste la opción 1")
  print("Adios")
elif opcion == 2:
  print("Hola")
  print("Cómo estás")
  print("Elegiste la opción 2")
  print("Adios")
elif opcion == 3:
  print("Hola")
  print("Cómo estás")
  print("Elegiste la opción 3")
  print("Adios")
else:
  print("Elige una opción correcta: (1, 2, o 3)")

# Sin Repetir Lógica
def conversacion(mensaje, despedida):
  print("Hola")
  print("Cómo estás")
  print(mensaje)
  print(despedida)

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
  conversacion("Elegiste la opción 1", "Adios")
elif opcion == 2:
  conversacion("Elegiste la opción 2", "Bye")
elif opcion == 3:
  conversacion("Elegiste la opción 3", "See you")
else:
  print("Elige una opción correcta: (1, 2, o 3)")