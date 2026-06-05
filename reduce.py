#Operacion de reduccion a un conjunto de lementos

from functools import reduce

numeros = [1,2,3,4,5]

total = reduce(lambda x,y : (x + y) * 2, numeros)
print(total)