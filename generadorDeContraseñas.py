import random
alfanumerico = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789-_.,:;{+}[*]¿¡'?)(/&%$#!°|"
def imprimir_linea_horizontal(texto = None):
  linea_horizontal = "+--" *11 + "+"
  print(linea_horizontal)
  if texto:
    print(texto)
    print(linea_horizontal + "\n")
    print()

def opciones():
  imprimir_linea_horizontal()
  texto = print("Hola, por favor elije una opcion:")
  imprimir_linea_horizontal()
  print()
  texto = print("1.- Generar Contraseña  0.-Salir")
  print()

def generar(longitud):
  contraseña = ""
  for i in range(longitud):
    contraseña += random.choice(alfanumerico)
  return contraseña

def iniciar():
  opciones()
  respuesta = input()
  print()
  if respuesta == "1":
    imprimir_linea_horizontal()
    print("Elija la longitud de la contraseña:")
    imprimir_linea_horizontal()
    print()
    print("1.- Corta  2.- Mediana  3.- Larga" + "\n")
    respuesta = input()
    print()
    if respuesta == "1":
      print("Contraseña generada:", generar(8) + "\n")
    elif respuesta == "2":
      print("Contraseña generada:", generar(12) + "\n")
    elif respuesta == "3":
      print("Contraseña generada:", generar(64) + "\n")
  elif respuesta == "0":
    return
  else:
    iniciar()

