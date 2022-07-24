# contador = 0
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 1
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 3
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))



# En python primero definimos una función principal: run, en algunos casos main
# En python las variables se declaran en minúsculas y lowerdash o underscore p.ej limite = 1000
# En python las constantes se declaran em mayúsculas y lowerdash o underscore p.ej LIMITE = 1000
def run():
  LIMITE = 1000

  contador = 0
  potencia_2 = 2**contador
  while potencia_2 < LIMITE:
    print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
    contador = contador + 1
    potencia_2 = 2**contador



# En segundo lugar ponemos nuestro entry point
if __name__ == '__main__':
  run()