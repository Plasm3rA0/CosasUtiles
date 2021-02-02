while True:
    try:
        numero = int(input("Introduce el numero que quieras pasar a binario: "))
        def binario(decimal):
            binario = ""
            while decimal // 2 != 0:
                binario = str(decimal % 2) + binario
                decimal = decimal // 2
            return str(decimal) + binario
        print(binario(numero))
    except:
        print("That's not a number")