
def numMax(num1, num2):
    if num1 > num2:
        Max = num1
    else:
        Max = num2
    return print("El mayor número Ingresado fue el ",Max)

a = int(input("Ingrese un número"))
b = int(input("Ingrese otro número para comparar"))
numMax(a, b)