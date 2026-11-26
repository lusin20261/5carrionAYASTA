from click import option


print("======================================================")
print("==========mi calculadora de la marca pajaro===========")
print("======================================================")

while True:
    print("")
    print("operacion que quieras")
    print("sumar")
    print("restar")
    print("multiplicacion")
    print("divicion")
    print("-------------------------------")

    opcion = input("elige la option q desees")

    if (opcion == "1"):
        num1 = input("ingresa el primer numero ")
        num1 = int("num1")
        num2 = input("ingresa el segundo numero")
        num2 = int("num2")
        print("el resultado es", num1 + num2)

    elif opcion == "2":
        num1 = input("ingresa el primer numero")
        num1 = int("num1")
        num2 = input("ingresa el segundo numero")
        num2 = int("num2")
        print("el resultado es",num1)
        