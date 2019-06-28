##a_len = 0
##b_len = 0
##a = "nada"
##b = ""
def superposicion(a,b, len):
    for i in range(len):
        c = b[i] in a
        print(c)
        if c == "True":
            print("TRUE")
        else:
            print("False")
            exit()

def Words():
    a = str(input("Ingrese su 1° Palabra"))
    a_len = len(a)
    b = str(input("Ingrese su 2° Palabra"))
    b_len = len(b)
    return a_len


##len = int(Words())
a = str(input("Ingrese su 1° Palabra"))
a_len = len(a)
b = str(input("Ingrese su 2° Palabra"))
b_len = len(b)
print(len)
print(a)
if a_len == b_len:
    superposicion(a, b, a_len)
else:
    len = Words()
