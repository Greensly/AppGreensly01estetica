def maxOf3(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        numMax = num1
    else:
        if num2 >= num3:
            numMax = num2
        else:
            numMax = num3
    return print("El mayor número es el ",numMax)
a = int(input("Ingrese el primer número"))
b = int(input("Ingrese un segundo número"))
c = int(input("Ingrese un tercer número"))
maxOf3(a, b, c)