mi_tupla = (1,  False, 'Jesus', 0.145)

print(mi_tupla[3])
print(type(mi_tupla))


def retornar_estudiante():
    return 'Jesus',28,8.6

tupla_estudiante = retornar_estudiante()
print(tupla_estudiante)

nombre_estudiante, edad_estudiante, promedio_estudiante = retornar_estudiante()

print(nombre_estudiante)
print(edad_estudiante)
print(promedio_estudiante)

#ONE LINE SWAPING = cambio de variables en una sola linea

#forma dificil
variable_1 = 1.0
variable_2 = 2.0

variable_temp = variable_1
variable_1 = variable_2
variable_2 = variable_temp

print(variable_1,variable_2)

#forma facil y correcta de hacer one line swaping

variable_1, variable_2 = variable_2, variable_1
print(variable_1,variable_2)