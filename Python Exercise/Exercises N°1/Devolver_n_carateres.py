def devolver_n_caracteres(n,c):
    caracter = ""
    for i in range(n):
        caracter += c
    return print(caracter)

letra = str(input("Ingrese el caracter a multiplicar"))
cantidad = int(input("Ingrese la cantidad a multiplicar el caracter"))
devolver_n_caracteres(cantidad,letra)