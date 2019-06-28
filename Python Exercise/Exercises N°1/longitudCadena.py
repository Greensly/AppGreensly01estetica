matriz = []

filas = int(input("Cantidad de Filas: "))
Columnas = int(input("Cantidad de Columnas: "))
for i in range(filas):
    matriz.append([0]*Columnas)

for x in range (filas):
    for y in range(Columnas):
        matriz[x][y]= int(input("Ingrese número para fila: [%i] columna [%i]"%(x,y)))

print (matriz)
print (len(matriz))
#print (matriz[0][0])
#print (matriz[0][1])
#print (matriz[0][2])
#print (matriz[0][3])

"""Otro tipo de comentario"""