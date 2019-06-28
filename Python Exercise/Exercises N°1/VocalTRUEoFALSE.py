def vocal(vocal):
    if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u' or vocal == 'A' or vocal == 'E' or vocal == 'I' or vocal == 'O' or vocal == 'U':
        x = "TRUE"
    else:
        x = "FALSE"
    return print(x)
a = input("Ingrese un caracter")
vocal(a)