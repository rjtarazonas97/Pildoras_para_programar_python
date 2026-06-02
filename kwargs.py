def conectar_bd(**kwargs):
    nombre = kwargs.get('nombre_db', 'default')
    user = kwargs ['usuario']
    password = kwargs ['password']
    port = kwargs ['password']
    dir_bd = kwargs ['dir_bd']
    print(f"Conectando con la base de datos {nombre}")
    print(f"login with: {user} - {password}")
    
conectar_bd(
            nombre_db = 'Produccion',
            usuario = 'root',
            password = '1234',
            port = 5002,
            dir_bd = '10.25.47.3',
            query = "SELECT * FROM tabla"
            )
