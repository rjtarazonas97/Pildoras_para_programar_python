# =========================
# SCOPE GLOBAL
# =========================

nombre = "Edward"

def imprimir_nombre_global():
    global nombre
    nombre = "Carlos"
    print(f"Hola como estas {nombre}")

imprimir_nombre_global()
print(f"El valor de mi variable global es {nombre}")


print("\n=========================")
print("SCOPE LOCAL")
print("=========================")

# =========================
# SCOPE LOCAL
# =========================

def imprimir_nombre_local():
    local = "Juan"
    print(f"Hola {local} como estas?")

imprimir_nombre_local()

# Esto generaría error porque la variable local
# solo existe dentro de la función
# print(f"Hola {local} como estas")


print("\n=========================")
print("SCOPE ENCLOSING")
print("=========================")

# =========================
# SCOPE ENCLOSING
# =========================

def imprimir_nombre():
    nombre_local = "Edward"
    edad_local = 30

    print(f"Hola {nombre_local} como estas?")

    def imprimir_edad():
        nonlocal edad_local
        edad_local = 40
        print(f"Su edad es {edad_local}")

    imprimir_edad()
    print(f"Edad es igual a {edad_local}")

imprimir_nombre()