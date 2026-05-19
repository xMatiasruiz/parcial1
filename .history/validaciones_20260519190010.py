from utilidades import es_letra, es_numero, simbolo_ascii

def validar_estructura(password:str) -> bool:
    """
    Valida los requisitos obligatorios de ingreso:
    no deja vacios, minimo 8 caracteres, no deja empezar con espacio y almenos una letra.
    Args:
        password (str): La cadena de texto de la contraseña a validar.

    Returns:
        bool: True si pasa todas las reglas de estructura, False si viola alguna.

    """
    largo = len(password)
    if largo == 0:
        print("[Error]La contraseña no puede estar vacia.")
        return False
    if largo < 8:
        print("[Error]: La contraseña debe tener al menos 8 caracteres")
        return False
    if password[0] == " ":
        print("[Error] La contraseña no puede comenzar con espacios.")
        return False
    
    tiene_letra = False
    for i in range(largo):
        if es_letra(password[i]):
            tiene_letra = True
    
    if not tiene_letra:
        print("[Error] La contraseña debe contener al menos una letra")
        return False
    
    return True


def contar_tipos(password:str):
    """
    Recorre manualmente la cadena y cuenta letras, numeros, simbolos y espacios.
    Args:
        password (str): La contraseña activa en el sistema.

    Returns:
        list: Una lista con cuatro enteros que representan [letras, números, símbolos, espacios]
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    for i in range(len(password)):
        caracter= password[i]
        if es_letra(caracter):
            letras+=1
        elif es_numero(caracter):
            numeros +=1
        elif simbolo_ascii(caracter):
            simbolos += 1
        elif caracter == " ":
            espacios += 1
    
    return [letras, numeros, simbolos, espacios] 