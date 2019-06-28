


InputChain = str(input("Ingrese una palabra o frase"))
OutputChain = ""
sizeChain = len(InputChain)
print(sizeChain)
for i in range(sizeChain):
    OutputChain += InputChain[sizeChain-1-i]
print("La palabra o frase original es: ",InputChain)
print(" y al invertirla que en:",OutputChain)