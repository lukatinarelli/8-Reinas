import os

tablero = [["-" for _ in range(9)] for _ in range(9)]

for i, letra in enumerate("ABCDEFGH"):
    tablero[i][8] = str(8 - i)
    tablero[8][i] = letra  


reinas = []

reinas.append(input("\033[32m¿En que posición quiere poner la primera reina? (Ej: A7, C2...) \033[m").upper())

for i, letra in enumerate("ABCDEFGH"):
    if reinas[0][0] == letra:
        tablero[8 - int(reinas[0][1])][i] = "\033[31mX\033[m"


#os.system('cls' if os.name == 'nt' else 'clear')

#-----------------------------------------------------------------------------------------------------------------------

#def colocar_reina(tablero, reinas):
    #código


print(tablero)

print(reinas)

for fila in tablero:
    print(" ".join(fila))