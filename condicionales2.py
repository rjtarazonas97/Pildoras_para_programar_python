# edad = 300

# if edad >= 0 and edad <=12:
#     print("Usted es un niño")
# elif edad >= 13 and edad <=17:
#     print("Usted es un adolecente")
# elif edad >=18 and edad <=59:
#     print("Usted es un adulto")
# else:
#     print("Usted es un adulto mayor")       


#if else anidado


# Desarrolla un Script que pida la edad y altura del usuario
# Si la persona es mayor de edad puede participar
# Pero la persona debe medir mas de 170
# Si la persona no mide 170 podra participar si es mayor a 25 años 
# y si altura es mayor a 165

edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu estatura: "))

if edad >= 18 and altura > 1.70:
    print("Si puedes participar")
elif edad >=25 and altura > 1.65:
    print("Si puede participar")
else:
    print("No puede participar")
26

# Como lo haria el profe pildora

edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu estatura: "))

if edad >=18:
    if(altura >= 1.70) or (edad >= 25 and altura >= 1.65):
        print("Puedes participar en el equipo de baloncesto")
    else:
        print("No cumples con lo requisitos para el equipo de baloncesto")
else:
    print("Debes ser mayor de edad para participar en el equipo de baloncesto")
    