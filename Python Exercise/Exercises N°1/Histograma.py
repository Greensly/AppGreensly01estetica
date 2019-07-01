def histograma(n1,n2,n3):
    a = ""
    b = ""
    d = ""
    for i in range(n1):
        a += "*"
    for i in range(n2):
        b += "*"
    for i in range(n3):
        d += "*"
    return print('{}\n{}\n{}' .format(a, b, d))

h1 = int(input("indique la cantidad de repeticiones de primer item"))
h2 = int(input("indique la cantidad de repeticiones de segundo item"))
h3 = int(input("indique la cantidad de repeticiones de tercer item"))

histograma(h1,h2,h3)
