def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra (mayuscula o minuscula)
    Args:
        caracter (str): El carácter individual a analizar.

    Returns:
        bool: True si pertenece al rango alfabético 'A'-'Z' o 'a'-'z', False en caso contrario.
    """
    mayus = "A" <= caracter <= "Z"
    minus = "a" <= caracter <= "z"
    return mayus or minus

def es_numero(caracter:str) -> bool:
    """
    Verifica si un caracter es un numero digito
    Args:
        caracter (str): El carácter individual a analizar.

    Returns:
        bool: True si está entre '0' y '9', False en caso contrario.
    
    """

    return "0" <= caracter <= "9"

def simbolo_ascii(caracter:str) -> bool:
    """
    Verifica si el caracter pertenece al grupo de simbolos ascii
    Args:
        caracter (str): El carácter individual a analizar.

    Returns:
        bool: True si su código ASCII está entre 33 y 47, False en caso contrario.
    """
    codigo = ord(caracter)
    return 33 <= codigo <= 47