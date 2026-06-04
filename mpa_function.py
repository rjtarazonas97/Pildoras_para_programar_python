
#Map es una funcion de orden superior
lista_nombre = ['maria','carlos','pepe']

lista_nombre_mayus = list(map(str.upper,lista_nombre))

print(lista_nombre_mayus)


lista_frutas = ['banano', 'pera', 'manzana', 'uva']

sufix = '_fruta'

lista_frutas_sufix = list(map(lambda x : x+sufix,lista_frutas))
print(lista_frutas_sufix)