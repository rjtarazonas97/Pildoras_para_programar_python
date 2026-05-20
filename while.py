nombre = ""
corre = ""
mensaje = ""

condicion_salida = "CONTINUE"

while condicion_salida == "CONTINUE":# WHILE significa mientras
    nombre = input("Por favor ingrese su nombre: ")
    correo = input("Por favor ingrese su correo: ")
    mensaje = input("Por favor ingrese el mensaje a enviar: ")
    
    print(f"""
          
          Mensaje enviado a {nombre}.
          
          Destinatario: {correo}.
          
          mensaje a enviar: {mensaje}
          
          """)
    
    condicion_salida = input("en caso de querer continuar con el programa escriba CONTINUE: ")
    

