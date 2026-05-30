#Ejemplo
def sumar(numero1, numero2):
    return numero1 + numero2

def sumar_tres(numero1, numero2, numero3):
    return numero1 + numero2 + numero3

resultado = sumar_tres(3,5,4)
print(f"El resultado es {resultado}")

#Forma correcta
def sumar(*args):
    print(type(args))
    return sum(args)

resultado = sumar(2,1,1,2)
print(f"El resultado es: {resultado}")


def sumar(*args):
    resultado = 0
    for element in args:
        resultado += element
        return resultado

resultado = sumar(2,1,1,2)
print(f"El resultado es: {resultado}")