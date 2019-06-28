def sum(a,b,c,d):
    sumTotal= a+b+c+d
    return print("La suma de todos los números da: ",sumTotal)

def mult(a,b,c,d):
    multTotal= a*b*c*d
    return print("La multiplicación de todos los números da:",multTotal)

def Choose():
    Answer = int(input("¿Que quiere hacer con estos números? SUMAR = 1 o MULTIPLICAR = 2 , Elija"))
    if Answer == 1:
        sum(a,b,c,d)
    elif Answer == 2:
        mult(a,b,c,d)
    elif Answer != 1 and Answer != 2:
        print ("Ingrese una de las dos opciones")
        Choose()
    return

a = int(input("Ingrese un número"))
b = int(input("Ingrese un 2° número"))
c = int(input("Ingrese un 3° número"))
d = int(input("Ingrese un 4° número"))
Choose()