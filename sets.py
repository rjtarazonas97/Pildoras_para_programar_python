#Declaracion

# mi_set = {1,2,3,4,5}
# print(mi_set)

# mi_set = set()
# mi_set.add(1)
# mi_set.add(2)
# mi_set.add(3)
# mi_set.add(4)
# print(mi_set) # Los sets no permiten datos duplicados

lista_numeros = [1,1,3,4,6,6,1,7] # Elimina elementos duplicados
mi_set = set(lista_numeros)
pertenece = 3 in lista_numeros
print(pertenece)

# fozenset

frutas = {'manzana',
          'platano',
          'pera',
          'uva'}

mi_frozenset = frozenset(frutas)
#mi_frozenset.add('naranja')
print(mi_frozenset)