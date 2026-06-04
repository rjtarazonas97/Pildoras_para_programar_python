numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(lambda x : x % 2 == 0,numbers))
print(lista_pares)


names = ["Alice","Bob","Anna","Davis","Amelia"]

retornar_nomnre_a = list(filter(lambda x : x[0] == 'A', names))
print(retornar_nomnre_a)