














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





