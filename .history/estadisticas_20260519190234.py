def generar_reporte(password):
    """
    Muestra longitudes, porcentajes y calcula repeticiones consecutivas.
    Args:
        password (str): La contraseña activa a procesar.

    Returns:
        Imprime el reporte técnico estructurado por pantalla.
    """

    largo = len(password)
    cant_letras, cant_numeros, cant_simbolos, cant_espacios = contar_tipos(password)

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