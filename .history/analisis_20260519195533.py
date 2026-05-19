def buscar_caracter(password, objetivo):
    """
    Busca un caracter especifico de forma manual informando cantidad y posiciones
    Args:
        contra (str): La contraseña original.

    Returns:
        str: La cadena de texto totalmente invertida.
    """

    contador = 0
    posiciones = ""

    for i in range(len(password)):
        if password[i] == objetivo:
            contador += 1
            posiciones = posiciones + str(i) + " "
    
    print(f"El caracter {objetivo} aparece {contador} veces")
    if contador > 0:
        print(f"Posiciones de aparicion:{posiciones}")

def invertir_password(contra:str) -> str:
    """
    Invierte la cadena utilizando un bucle que recorre de atras hacia adelante
    Args:
        contra (str): La cadena original a invertir.

    Returns:
        str: La cadena de texto totalmente invertida.
    """

    invertida = ""
    for i in range(len(contra) - 1, -1. -1):
        invertida = invertida + contra[i]
    return invertida

def verificar_palindromo(password: str) -> bool:
    """
    Determina si es palindromo comparando los extremos hacia el centro
    Args:
        password (str): La contraseña a verificar.

    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    palindromo = True
    largo =len(password)
    for i in range(largo // 2):
        if password[i] != password[largo -1 -i]:
            palindromo = False
        return palindromo
    
def ordenar_password(password: str, ascendente:bool) -> str:
    """
    Ordena los caracteres mediante Bubble sort, basandose en el codigo ascii
    Args:
        password (str): La cadena original desordenada.
        ascendente (bool): True para orden menor a mayor, False para mayor a menor.

    Returns:
        str: Una nueva cadena con los caracteres totalmente ordenados.
    """
    largo = len(password)
    lista_caracteres = [""] * largo
    for i in range(largo):
        lista_caracteres[i] = password[i]
    
    for i in range (largo): 
        
        for j in range(0, largo - i -1):
            codigo_actual= ord(lista_caracteres[j])
            codigo_siguiente = ord(lista_caracteres[j+1])

            if ascendente:
                if codigo_actual > codigo_siguiente:
                    lista_caracteres[j], lista_caracteres[j + 1] = lista_caracteres[j + 1], lista_caracteres[j]
            else:
                if codigo_actual < codigo_siguiente:
                    lista_caracteres[j], lista_caracteres[j + 1] = lista_caracteres[j + 1], lista_caracteres[j]
            
    resultado = ""
    for i in range(largo):
        resultado = resultado + lista_caracteres[i]
    return resultado

