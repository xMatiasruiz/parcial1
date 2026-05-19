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