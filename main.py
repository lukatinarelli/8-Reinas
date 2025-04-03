
tablero = [["-" for _ in range(9)] for _ in range(9)]

for i, letra in enumerate("ABCDEFGH"):
    tablero[i][8] = str(8 - i)
    tablero[8][i] = letra  


reinas = []

reinas.append(input("¿En que posición quiere poner la primera reina? (Ej: A7, C2...) ").upper())


def colocar_reina(tablero, reinas):
    #código


print(tablero)

print(reinas)

for fila in tablero:
    print(" ".join(fila))
