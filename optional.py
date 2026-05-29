def calcular_precio(nombre_producto, cantidad, precio_u, descuento = 0):
    precio_final = (cantidad * precio_u) * (1-descuento)
    print(f"El precio final para {nombre_producto} es {precio_final}")
    
calcular_precio("Camisa", 3, 20, 0.20)