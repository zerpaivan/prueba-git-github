# script para realizar operaciones matematicas basicas
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


if __name__ == "__main__":

    a = 5
    b = 0
    print("suma: ", sumar(a, b))
    print("resta: ", restar(a, b))
    print("multiplicacion: ", multiplicar(a, b))
    print("divivion: ", division(a, b))
