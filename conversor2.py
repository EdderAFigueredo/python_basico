while True:

    resultado = 0

    menu = int(input(''' 
    Menú Conversión de Moneda.
    \n \t [1] Dolar Australiano (AUD) To Peso Colombiano   (COP).
    \n \t [2] Peso Colombiano   (COP) To Dolar Australiano (AUD).
    \n \t [3] Dolar Americano   (USD) To Peso Colombiano   (COP).
    \n \t [4] Peso Colombiano   (COP) To Dolar Americano   (USD).
    \n Ingresa la opción de conversión que deseas: '''))
    
    if menu == 1:
        cantidad = int(input("\n Ingresa la cantidad de dolares australianos que quieres convertir: "))
        valor = 2822
        resultado = cantidad * valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} dolares australianos equivalen a ${resultado} pesos colombianos.")

    elif menu == 2:
        cantidad = int(input("\n Ingresa la cantidad de pesos colombianos que quieres convertir: "))
        valor = 2822
        resultado = cantidad / valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares australianos.")
    
    elif menu == 3:
        cantidad = int(input("\n Ingresa la cantidad de dolares americanos que quieres convertir: "))
        valor = 3815
        resultado = cantidad * valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} dolares americanos equivalen a ${resultado} pesos colombianos.")

    elif menu == 4:
        cantidad = int(input("\n Ingresa la cantidad de pesos colombianos que quieres convertir: "))
        valor = 3815
        resultado = cantidad / valor
        resultado = round(resultado, 2)
        print(f"\n \t ${cantidad} pesos colombianos equivalen a ${resultado} dolares americanos.")

    else:
        print("\n \t Ingresa una opción válida")

    resetmenu = int(input("\n \n ¿Deseas usar de nuevo el conversor? [1] Yes / [2] No : "))

    if resetmenu == 2:
        exit()
    else:
        menu = ""