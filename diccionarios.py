#Declarar un diccionario

mi_diccionario = {
    'Jesus':[1.4,4.5,5.0],
    'Carla':[4.4,5.0,5.0],
    'Jonas':[0.0,3.4,3.0]
}

mi_diccionario['Maria'] = [1.3, 2.4, 4.4]

del mi_diccionario['Jesus'] # De esta manera se puede borrar un objeto dentro d eun diccionario

#Metodo Dict

mi_diccionario_2 = dict(Jesus = [1.4,4.5,5.0],
                        Carla = [1.4,4.5,5.0],
                        Jonas =[1.4,4.5,5.0])

#dict_vacio

mi_diccionario_3 = dict()
mi_diccionario_3['Jesus'] = [1.4,4.5,5.0]
mi_diccionario_3['Carla'] = [1.4,4.5,5.0]
mi_diccionario_3['Jonas'] = [1.4,4.5,5.0]



print(mi_diccionario)
print(mi_diccionario_2)
print(mi_diccionario_3)
print(mi_diccionario['Jonas'])



#Metodos keys

print(mi_diccionario.keys())

#Metodo Values

print(mi_diccionario.values())

#both

print(mi_diccionario.items())