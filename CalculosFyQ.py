import math
import os

###INDICE###
print("1:  Si quieres saber el trabajo ingresando Fx y distancia")
print("2:  Si quieres encontrar el trabajo ingresando fuerza, grados y distància")
print("3:  Si quieres sumar fuerzas ingresando fuerzas y grados")
print("4:  Operaciones fàciles")

###CODIGO###
code = int(input("Que codigo quieres realizar?"))
#1#
if code == 1:
    FuerzaEnX = int(input("Fuerza en X: "))
    Distancia = int(input("Distancia: "))
    print("El resultado és: {} Julios".format(FuerzaEnX*Distancia))
#2#
elif code == 2:
    Fuerza = int(input("Fuerza: "))
    Grados = int(input("Grados: "))
    Distancia = int(input("Distancia: "))
    FuerzaEnX = Fuerza*math.cos(math.radians(Grados))
    if FuerzaEnX <= 0.000000001:
        print("El resultado és 0 Julios")
    else:
        print("El resultado és: {} Julios".format(FuerzaEnX * Distancia))
#3#
elif code ==3:
    F1ENTRED = int(input("F1: "))
    G1ENTRED = int(input("Grados F1: "))
    F2ENTRED = int(input("F2: "))
    G2ENTRED = int(input("Grados F2: "))
    F1x = math.cos(math.radians(G1ENTRED))*F1ENTRED
    F2x = math.cos(math.radians(G2ENTRED))*F2ENTRED
    FRx = F1x+F2x
    F1y = math.sin(math.radians(G1ENTRED))*F1ENTRED
    F2y = math.sin(math.radians(G2ENTRED))*F2ENTRED
    FRy = F1y+F2y
    FR = math.sqrt(FRy*FRy+FRx*FRx)
    print("La fuerza resultante és de {} Newtons".format(FR))
#4#
elif code ==4:
    os.system("cls")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    print("5: Un numero elevado a otro")
    print("6: Raíz cuadrada de un numero")
    type = int(input("Que quieres hacer?"))
    if type == 1:
        Num1 = int(input("Primer Numero: "))
        Num2 = int(input("Segundo Numero: "))
        Result = Num1+Num2
    elif type ==2:
        Num1 = int(input("Primer Numero: "))
        Num2 = int(input("Segundo Numero: "))
        Result = Num1-Num2
    elif type ==3:
        Num1 = int(input("Primer Numero: "))
        Num2 = int(input("Segundo Numero: "))
        Result = Num1*Num2
    elif type ==4:
        Num1 = int(input("Primer Numero: "))
        Num2 = int(input("Segundo Numero: "))
        Result = Num1/Num2
    elif type ==5:
        Num = int(input("Numero:"))
        Expo = int(input("Exponente: "))
        Result = Num
        for x in range(Expo):
            Result = Result*Num
    elif type == 6:
        Num = int(input("Numero:"))
        Radi = int(input("Radical: "))
        Result = Num
        for x in range(Radi):
            Result = Result/Num
    else:
        print("Elije un valor apropiado")
    try:
        print("El resultado és: {}".format(Result))
    except:
        print('vuelve a iniciar el programa')
