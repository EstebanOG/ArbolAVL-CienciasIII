import pathlib
from pathlib import Path


# Clase Nodo
class Nodo:
  # Constructor
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None


# Clase Pila
class Pila:
  # Constructor
  def __init__(self):
    self.superior = None

  # Método apilar
  def apilar(self, dato):
    # Si no hay datos, agregamos el valor en el elemento superior y regresamos
    if self.superior == None:
      self.superior = Nodo(dato)
      return
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = self.superior
    self.superior = nuevo_nodo

# Método desapilar

  def desapilar(self):
    # Si no hay datos en el nodo superior, regresamos
    if self.superior == None:
      print("No hay ningún elemento en la pila para desapilar")
      return
    self.superior = self.superior.siguiente

  # Método imprimir
  def imprimir(self):
    # Recorrer la pila e imprimir valores
    nodo_temporal = self.superior
    datos = ""
    while nodo_temporal != None:
      datos = datos + f"{nodo_temporal.dato}\n"
      nodo_temporal = nodo_temporal.siguiente
    return datos


# Método Main
class Main:
  # Constructor
  def __init__(self):
    self.flag = True
    # Crear pila
    self.pila = Pila()
    # Crear el archivo si no existe
    myfile = Path('datos.txt')
    myfile.touch(exist_ok=True)
    f = open(myfile)
    mensaje = f.readlines()
    for texto in mensaje:
      texto = texto.rstrip()
      if texto != "":
        self.pila.apilar(texto)
    f.close()

  # Método menu
  def menu(self):
    while self.flag:
      print("\nMenu")
      print("1. Apilar datos")
      print("2. Desapilar datos")
      print("3. Consultar archivo de texto")
      print("4. Salir")
      op = int(input("Ingrese su opcion: "))
      if op == 1:
        self.apilar_datos()
      elif op == 2:
        self.desapilar_datos()
      elif op == 3:
        self.consultar_archivo()
      elif op == 4:
        self.flag = False

  # Método para apilar datos
  def apilar_datos(self):
    contenido = input("\nIngrese los datos que desea apilar en el archivo: ")
    self.pila.apilar(contenido)
    datos = self.pila.imprimir()
    f = open('datos.txt', 'w')
    f.write(datos)
    f.close()

  # Método para apilar datos
  def desapilar_datos(self):
    self.pila.desapilar()
    datos = self.pila.imprimir()
    f = open('datos.txt', 'w')
    f.write(datos)
    f.close()

  # Método consultar_archivo
  def consultar_archivo(self):
    f = open('datos.txt', 'r')
    mensaje = f.read()
    if mensaje == '':
      print('\nEl archivo no contiene datos.\n')
    else:
      print(mensaje)
    f.close()


if __name__ == '__main__':
  main = Main()
  main.menu()
