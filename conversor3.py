while True:
    
    def conversor_aud_to_cop():
        cantidad = int(input("\n Ingresa la cantidad de dolares australianos que quieres convertir: "))
        valor = 2822
        resultado = cantidad * valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares australianos.")

    def conversor_cop_to_aud():
        cantidad = int(input("\n Ingresa la cantidad de pesos colombianos que quieres convertir: "))
        valor = 2822
        resultado = cantidad / valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares australianos.")

    def conversor_usd_to_cop():
        cantidad = int(input("\n Ingresa la cantidad de dolares americanos que quieres convertir: "))
        valor = 3815
        resultado = cantidad * valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} dolares americanos equivalen a ${resultado} pesos colombianos.")
    
    def conversor_cop_to_usd():
        cantidad = int(input("\n Ingresa la cantidad de pesos colombianos que quieres convertir: "))
        valor = 3815
        resultado = cantidad / valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares americanos.")

    def resetmenu():
        resetmenu = int(input("\n \n ¿Deseas usar de nuevo el conversor? [1] Yes / [2] No : "))
        if resetmenu == 2:
            exit()
        else:
            menu = ""

    resultado = 0


    menu = int(input(''' 
    Menú Conversión de Moneda.
    \n \t [1] Dolar Australiano (AUD) To Peso Colombiano   (COP).
    \n \t [2] Peso Colombiano   (COP) To Dolar Australiano (AUD).
    \n \t [3] Dolar Americano   (USD) To Peso Colombiano   (COP).
    \n \t [4] Peso Colombiano   (COP) To Dolar Americano   (USD).
    \n Ingresa la opción de conversión que deseas: '''))
    
    if menu == 1:
        conversor_aud_to_cop()
        # cantidad = int(input("\n Ingresa la cantidad de dolares australianos que quieres convertir: "))
        # valor = 2822
        # resultado = cantidad * valor
        # resultado = round(resultado, 2)
        # print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares australianos.")

    elif menu == 2:
        conversor_cop_to_aud()  
    elif menu == 3:
        conversor_usd_to_cop()
    elif menu == 4:
        conversor_cop_to_usd()
    else:
        print("\n \t Ingresa una opción válida")

    resetmenu()