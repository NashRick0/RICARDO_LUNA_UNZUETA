import math

def area_circulo(radio):
    area = math.pi * radio*radio
    return area

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_cuadrado(lado):
    area = lado*lado
    return area

def menu():
    print("MENU")
    print("A. Circulo")
    print("B. Rectangulo")
    print("C. Cuadrado")
    print("D. Salir")

def opciones():
    while True:
        menu()
        opcion = input("Seleccione la opcion para sacar el area: ")
        
        if opcion == 'A':
            radio = float(input("Ingrese el radio del circulo: "))
            print("El area del circulo es:", area_circulo(radio))
        elif opcion == 'B':
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            print("El area del rectangulo es:", area_rectangulo(base, altura))
        elif opcion == 'C':
            lado = float(input("Ingrese el lado del cuadrado: "))
            print("El area del cuadrado es:", area_cuadrado(lado))
        elif opcion == 'D':
            print("Saliendo")
            break
opciones()

