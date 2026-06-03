# def retornar_nota(estudiante):
#     return estudiante[1]

lista_estudiantes = [('Jesus', 4.2),
                     ('Pepe',2.2),
                     ('Maria',3.1),
                     ('Carlos',4.5)] 

lista_ordenada = sorted(lista_estudiantes,key= lambda x:x[1],reverse=True)
print(lista_ordenada)