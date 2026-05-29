def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    
    print(f"Hola {primer_nombre} {segundo_nombre} "\
          f"{primer_apellido} {segundo_apellido} " \
              " Bienvenido al curso de python")
    
    
#Positional Args
imprimir_nombre("Rodnyn", "Jesús", "Tarazona", "Sanchez")

#Keywords Args 
imprimir_nombre(primer_nombre="Rodnyn",segundo_nombre="Jesús",
                 primer_apellido=" Tarazona", segundo_apellido="Sanchez")
imprimir_nombre("Rodnyn","Jesús",segundo_apellido="Sanchez",primer_apellido=" Tarazona")

#Iterable unpacking
estudiante = ("Carlos", "Alberto", "Gomez", "Rojas")
imprimir_nombre(*estudiante) # Se agrega una asterisco antes para que la tupla acceda a la funcion imprimir_nombre

#Dictionary unpacking
estudiante_dick = {
    'primer_apellido' : 'Gomez',
    'primer_nombre' : 'Carlos',
    'segundo_nombre' : 'Alberto',
    'segundo_apellido' : 'Rojas'
}

imprimir_nombre(**estudiante_dick)



