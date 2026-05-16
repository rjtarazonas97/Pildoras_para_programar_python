# #USando Listas
# lista_elementos = [1,2,3,4,5]

# for elemento in lista_elementos:
#     print(lista_elementos)
    
# # Usando for range

# for _ in range (4):
#     print("desde origen avanzar 10 pasos")
#     print("girar 90 grados")
    
lista_nombres = ['Jesus', 'Juan', 'Maria']

# for indice in range(3):
#     print(indice, lista_nombres[indice])
    
    
# Forma correcta enumarate

lista_nombres = ['Jesus', 'Juan', 'Maria']

for indice, valor in enumerate(lista_nombres):
    print(indice, valor)