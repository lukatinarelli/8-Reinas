import os

QUEEN_MARKER = "\033[31mX\033[m"
tablero = [["-" for _ in range(9)] for _ in range(9)]

for i, letra in enumerate("ABCDEFGH"):
    tablero[i][8] = str(8 - i)
    tablero[8][i] = letra  


reinas = []

reinas.append(input("\033[32m¿En que posición quiere poner la primera reina? (Ej: A7, C2...) \033[m").upper())

for i, letra in enumerate("ABCDEFGH"):
    if reinas[0][0] == letra:
        tablero[8 - int(reinas[0][1])][i] = QUEEN_MARKER


#os.system('cls' if os.name == 'nt' else 'clear')

#-----------------------------------------------------------------------------------------------------------------------

def colocar_reina(tablero, reinas):
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna] == "-":
                # Comprobar si puede colocar la reina
                if puede_colocar_reina(tablero, fila, columna):
                    tablero[fila][columna] = QUEEN_MARKER
                    reinas.append((fila, columna))
                    # Intentar colocar la siguiente reina
                    if colocar_reina(tablero, reinas):
                        return True
                    # Si no se puede colocar la siguiente reina, quitar la actual
                    tablero[fila][columna] = "-"
                    reinas.pop()
                    
    # Si no se pudo colocar todas las reinas, devolver False
    return len(reinas) == 8

def puede_colocar_reina(tablero, fila, columna):
    # Comprobar filas y columnas
    for i in range(8):
        if tablero[fila][i] == QUEEN_MARKER or tablero[i][columna] == QUEEN_MARKER:
            return False

    # Comprobar diagonales
    for offset in range(-7, 8):
        if 0 <= fila + offset < 8 and 0 <= columna + offset < 8 and tablero[fila + offset][columna + offset] == QUEEN_MARKER:
            return False
        if 0 <= fila + offset < 8 and 0 <= columna - offset < 8 and tablero[fila + offset][columna - offset] == QUEEN_MARKER:
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
