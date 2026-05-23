#Mi primera Calculadora en python

def sumar(numero1,numero2):
    resultado = numero1 + numero2
    print(f"La suma entre {numero1} y {numero2} es igual a: {resultado}")
    
def restar(numero1,numero2):
    resultado = numero1 - numero2
    print(f"La resta entre {numero1} y {numero2} es igual a: {resultado}")
        
def multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    print(f"La multiplicacion entre {numero1} y {numero2} es igual a: {resultado}")
    
def dividir(numero1,numero2):
    resultado = numero1 / numero2
    print(f"La division entre {numero1} y {numero2} es igual a: {resultado}")


primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese sel tipo de operacion a realizar: ")

if operacion == 'sumar':
    sumar(primer_numero,segundo_numero)
elif operacion == 'restar':
    restar(primer_numero,segundo_numero)
elif operacion == 'multiplicar':
    multiplicar(primer_numero,segundo_numero)
elif operacion == 'dividir':
    dividir(primer_numero,segundo_numero)
else:
    print("Por favor ingrese una operacion valida"\
        "sumar, restar, multiplicar o dividir")