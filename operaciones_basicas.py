# script para realizar operaciones matematicas basicas
from math import sqrt


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division por cero no permitida"


def potencia(a, b):
    return a ** b


# funcion creada desde la rama de prueba
def raiz_cuadrada(a, b):
    return sqrt(a)


if __name__ == "__main__":

    a = 5
    b = 0
    print("suma: ", sumar(a, b))
    print("resta: ", restar(a, b))
    print("multiplicacion: ", multiplicar(a, b))
    print("divivion: ", division(a, b))
    print("potencia: ", potencia(a, b))
    print(f"raiz_cuadrada {a}: {raiz_cuadrada(a)}")

# se añade texto e la rama main
# rama main
