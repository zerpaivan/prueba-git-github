# script para realizar operaciones matematicas basicas
from math import sqrt


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


# funcion creada desde la rama de prueba
def raiz_cuadrada(a, b):
    return sqrt(a)


if __name__ == "__main__":

    a = 5
    b = 4
    print("suma: ", sumar(a, b))
    print("resta: ", restar(a, b))
    print("multiplicacion: ", multiplicar(a, b))
    print(f"raiz cuadrada de {a}: {raiz_cuadrada(a)}")
