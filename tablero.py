
columnas =  8
filas = 8


tablero = [["-" for _ in range(columnas)] for _ in range(filas)]

print(tablero)

for fila in tablero:
    print(" ".join(fila))
print()