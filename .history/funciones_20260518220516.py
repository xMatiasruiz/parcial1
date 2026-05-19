def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra (mayuscula o minuscula)

    """
    mayus = "A" <= caracter <= "Z"
    minus = "a" <= caracter <= "z"
    return mayus or minus

def es_numero(caracter:str) -> bool:
    """
    Verifica si un caracter es un numero digito
    """

    return "0" <= caracter <= "9"

def simbolo_ascii(caracter:str) -> bool:
    """
    Verifica si el caracter pertenece al grupo de simbolos ascii
    """
    codigo = ord(caracter)
    return 33 <= codigo <= 47

def contar_tipos(password:str):
    """
    Recorre manualmente la cadena y cuenta letras, numeros, simbolos y espacios.
    
    """

def validar_estructura(password:str) -> bool:
    """
    Valida los requisitos obligatorios de ingreso:
    no deja vacios, minimo 8 caracteres, no deja empezar con espacio y almenos una letra.
    """
    largo = len(password)
    if largo == 0:
        print("[Error]La contraseña no puede estar vacia.")
        return False
    if largo < 8:
        print("[Error]: La contraseña debe tener al menos 8 caracteres")
    if password[0] == " ":
        print("[Error] La contraseña no puede comenzar con espacios.")
    
    tiene_letra = False
    for i in range(largo):
        if es_letra(password[i]):
            tiene_letra = True
    
    if not tiene_letra:
        print("[Error] La contraseña debe contener al menos una letra")
        return False
    
    return True

def validar_nivel_seguridad(password:str) -> str:
    """
    Determina el nivel de seguridad analizando la longitud y tipos de caracteres.
    """

    largo = len(password)
    cant_letras, cant_numeros, cant_simbolos, cant_espacios = contar_tipos(password)

    if largo >= 12 and cant_letras > 0 and cant_numeros > 0 and cant_numeros > 0 and cant_simbolos > 0 and cant_espacios > 0:
        return "Fuerte"
    
    if 8 <= largo <= 9 and cant_letras == largo:
        return "Debil"
    
    return "Media"

def buscar_caracter(password, objetivo):
    """
    Busca un caracter especifico de forma manual informando cantidad y posiciones
    """

    contador = 0
    posiciones = ""

    for i in range(len(password)):
        if password[i] == objetivo:
            contador += 1
            posiciones = posiciones + str(i) + ""
    
    print(f"El caracter {objetivo} aparece {contador} veces")
    if contador > 0:
        print(f"Posiciones de aparicion:{posiciones}")

def invertir_password(contra:str) -> str:
    """
    Invierte la cadena utilizando un bucle que recorre de atras hacia adelante
    """

    invertida = ""
    for i in range(len(contra) - 1, -1. -1):
        invertida = invertida + contra[i]
    return invertida

def generar_reporte(password):
    """
    Muestra longitudes, porcentajes y calcula repeticiones consecutivas.
    """

    largo = len(password)
    cant_letras, cant_simbolos, cant_numeros = contar_tipos(password)

    letras = (cant_letras / largo) * 100
    numeros = (cant_numeros / largo) * 100
    simbolos = (cant_simbolos / largo) * 100

    print(f"Longitud total: {largo} caracteres")
    print(f"Porcentaje de letras: {letras}%")
    print(f"Porcentaje de numeros: {numeros}%")
    print(f"Porcentaje de simbolos: {simbolos}%")
    print("Analisis de caracteres repetidos consecutivos:")

    i = 0
    hubo_repeticiones = False
    while i < largo - 1:
        if password[i] == password[i+1]:
            caracter_repetido = password[i]
            contador_bloque = 0
            while i < largo - 1 and password[i] == password[i+1]:
                contador_bloque += 1
                i += 1
            print(f"-{contador_bloque} repeticion de {caracter_repetido}")
            hubo_repeticiones = True
        else:
            i += 1
    if not hubo_repeticiones:
        (print("- No se detectaron caracteres repetidos consecutivos."))


def verificar_palindromo(password: str) -> bool:
    """
    Determina si es palindromo comparando los extremos hacia el centro.
    """
    pal = True
    largo =len(password)


