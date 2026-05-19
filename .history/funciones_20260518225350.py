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
    Determina si es palindromo comparando los extremos hacia el centro
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

def mostrar_menu():
    """
    Imprime la interfaz
    """
    print("\n" + "="*40)
    print("  1. Ingresar contraseña")
    print("  2. Validar nivel de seguridad")
    print("  3. Contar tipos de caracteres")
    print("  4. Buscar carácter específico")
    print("  5. Mostrar contraseña invertida")
    print("  6. Generar reporte técnico (Estadísticas)")
    print("  7. Verificar si es palíndromo")
    print("  8. Ordenar caracteres de la contraseña")
    print("  9. Salir")
    print("="*40)

def main():
    """
    Funcion principal que coordina el flujo del sistema de procesamiento.
    """

    password_act = ""
    opcion = 0
    print("Bienvendo al Sistema de procesamiento de Contraseñas!!")

    while opcion != 9:
        mostrar_menu()
        ingreso_opcion = input("Seleccione una opcion(1-9): ")
        if len(ingreso_opcion) == 1 and "1" <= ingreso_opcion <= "9":
            opcion = int(ingreso_opcion)
        else:
            print("[Error] Opcion invalida. Intente de nuevo. ")
            continue

        if opcion != 1 and opcion !=9 and password_act == "":
            print("[Advertencia] Primero debe ingresar una contraseña (Opcion 1).")
            continue

        if opcion == 1:
            ingreso = input("Ingrese la nueva contraseña a procesar: ")
            if validar_estructura(ingreso):
                password_act= ingreso
                print("[OK] contraseña guardado con exito!!")
            
            elif opcion == 2:
                seguridad = validar_nivel_seguridad(password_act)
                print(f"El nivel de seguridad de la contraseña es: {seguridad}")
            
            elif opcion == 3:
                cant_letras, cant_numeros, cant_simbolos, cant_espacios = contar_tipos(password_act)
                print(f"Cantidad de letras: {cant_letras}")
                print(f"Cantidad de números: {cant_numeros}")
                print(f"Cantidad de símbolos: {cant_simbolos}")
                print(f"Cantidad de espacios: {cant_espacios}")
            
            elif opcion == 4:
                caracte_busqueda = input("Ingrese el unico caracter a buscar en la cadena: ")
                if len(caracte_busqueda) == 1:
                    buscar_caracter(password_act, caracte_busqueda)
                else:
                    print("[Error] Debe ingresar exactamente un solo caracter")
            
            elif opcion == 5:
                resultado_invertido = invertir_password(password_act)
                print(f"Contraseña original: {password_act}")
                print(f"Contraseña invertida: {resultado_invertido}")
            
            elif opcion == 6:
                generar_reporte(password_act)
            
            elif opcion == 7:
                if verificar_palindromo(password_act):
                    print(f"La contraseña {password_act} Si es un palindromo")
                else: 
                    print(f"La contraseña {password_act} No es un palindromo")
            
            elif opcion == 8:
                print("1. Orden ascendente (Ascii menor a mayor)")
                print("1. Orden descendente (Ascii mayor a menor)")
                seleccion_orden = input("Seleccione el tipo de orden (1 o 2): ")

                if seleccion_orden == "1":
                    ordenada = ordenar_password(password_act, True)
                    print(f"Resultado ascendente: {ordenada}")
                
                elif seleccion_orden == "2":
                    ordenada = ordenar_password(password_act, False)
                    print(f"Resultado descendente: {ordenada}")
                
                else:
                    print("[Error] Eleccion incorrecta. ")
                
            elif opcion == 9:
                print("Saliendo de la aplicacion. Buenas Noches!!1!")

main()





