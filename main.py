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

def colocar_reina(tablero, reinas):
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna] == "-":
                # Comprobar si puede colocar la reina
                if puede_colocar_reina(tablero, fila, columna, reinas):
                    tablero[fila][columna] = "\033[31mX\033[m"
                    reinas.append((fila, columna))
                    return True
    return False

def puede_colocar_reina(tablero, fila, columna, reinas):
    # Comprobar filas y columnas
    for i in range(8):
        if tablero[fila][i] == "\033[31mX\033[m" or tablero[i][columna] == "\033[31mX\033[m":
            return False

    # Comprobar diagonales
    for i in range(8):
        for j in range(8):
            if abs(fila - i) == abs(columna - j) and tablero[i][j] == "\033[31mX\033[m":
                return False

    return True

#-----------------------------------------------------------------------------------------------------------------------

#   for filas in ...
#   for columnas in ...
#       if puede haber reina
#           colocar reina
#       colocar_reina()
#       if colocar_reina() no coloca
#           quitar la ultima reina

colocar_reina(tablero, reinas)

print(tablero)

print(reinas)

for fila in tablero:
    print(" ".join(fila))
