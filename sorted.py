estudiantes = [
    ('Juana',22,95,'555-1234'),
    ('Pedro',18,89,'555-1234'),
    ('Juan',25,94,'555-1234')
]

lista_estudiante_edad = sorted(estudiantes,key= lambda x: x[1])
print(lista_estudiante_edad)