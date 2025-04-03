
tablero = [["-" for _ in range(9)] for _ in range(9)]

for i, letra in enumerate("ABCDEFGH"):
    tablero[i][8] = str(8 - i)
    tablero[8][i] = letra  


print(tablero)

for fila in tablero:
    print(" ".join(fila))
