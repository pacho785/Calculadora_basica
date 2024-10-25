bucle = True
while bucle:
    op = input("""Elija la operacion a realizar
    A.Suma 
    B.Resta
    C.Multiplicacion
    D.Division
    X.salir
    """).upper()

    if op=="A":
        print("---Suma---")

        num1 = int(input("Dijite el primer valor a sumar"))
        num2 = int(input("Dijite el segundo numero a sumar"))

        print(f"El resultado de la suma es: {num1+num2}")
    elif op=="B":
        print("---Resta---")

        num3 = int(input("Dijite el primer valor a restar"))
        num4 = int(input("Dijite el segundo numero a restar"))

        print(f"El resultado de la resta es: {num3-num4}")
    elif op=="C":
        print("---Multiplicacion---")

        num5 = int(input("Dijite el primer valor a multiplicar"))
        num6 = int(input("Dijite el segundo numero a multiplicar"))

        print(f"El resultado de la multiplicacion es: {num5*num6}")
    elif op=="D":
        print("---Division---")

        num7 = int(input("Dijite el primer valor a dividir"))
        num8 = int(input("Dijite el segundo numero a dividir"))

        print(f"El resultado de la division es: {num7*num8}")
    elif op=="X":

        print("SALIENDO DEL PROGRAMA")
    else:
        print("Opcion incorrecta vuelva a intentarlo")