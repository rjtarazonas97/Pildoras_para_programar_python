lista_numeros = [1,2,3,4]
lista_nombre = ['Jesus','Pedro','Juan']
lista_bool = [True, False, False]

print(lista_numeros[2])

lista_numeros[2] = 100
print(lista_numeros[2])
print(lista_numeros)
print(id(lista_numeros))


lista_numeros = list((1,2,3))
print(type(lista_numeros))

lista_numeros = [1,2,3]

#append (Agraga un objeto al final de tu lista)
lista_numeros.append(4)
lista_numeros.append(5)
lista_numeros.append(5)
print(lista_numeros)

#count (Cuenta c uantas objetos se repiten dentro de la lista)
print(lista_numeros.count(5))

#extend (Agraga otras listas a tu lista original sin usar append)
lista_extendida = [100,101]
lista_numeros.extend(lista_extendida)
print(lista_numeros)


#index (Cuenta en que posicion estas)

print(lista_numeros.index(100))

#Insert (Puedes agregar a tu lista objetos en la posicion que quierasy luego que valor le quieras dar)

print(lista_numeros)
lista_numeros.insert(0,5000)
print(lista_numeros)

#pop (Estrae elementos de la lista y los retorna)

print(lista_numeros.pop(0))
print(lista_numeros)

#remove (Elimina elemntos por valor)

lista_numeros.remove(100)
print(lista_numeros)

#reverse (Revierte la lista desde el final al inicio)
print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)

#Clear (Limpia totalmente la lista)

lista_numeros.clear()
print(lista_numeros)

#sort (Ordena la lista de menor a mayor)

lista_numeros = [4,3,2,1]
lista_numeros.sort()
print(lista_numeros)