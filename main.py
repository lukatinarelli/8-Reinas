import os, time

tablero = [["-" for _ in range(9)] for _ in range(9)]

for i, letra in enumerate("ABCDEFGH"):
    tablero[i][8] = str(8 - i)
    tablero[8][i] = letra  


reinas = []

reinas.append(input("\033[32m¿En que posición quiere poner la primera reina? (Ej: A7, C2...) \033[m").upper())

for i, letra in enumerate("ABCDEFGH"):
    if reinas[0][0] == letra:
        tablero[8 - int(reinas[0][1])][i] = "\033[31mX\033[m"
        reinas.append((8 - int(reinas[0][1]), i))
        reinas.pop(0)


os.system('cls' if os.name == 'nt' else 'clear')

for i in tablero:
    print(" ".join(i))

#-----------------------------------------------------------------------------------------------------------------------

def colocar_reina(tablero, reinas):
    if len(reinas) < 8:
        for fila in range(8):
            for columna in range(8):
                if tablero[fila][columna] == "-" and puede_colocar_reina(tablero, fila, columna, reinas):
                    tablero[fila][columna] = "\033[31mX\033[m"
                    reinas.append((fila, columna))

                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in tablero:
                        print(" ".join(i))
                    time.sleep(0.5)
                        
                    if colocar_reina(tablero, reinas):
                        return True
                
                    else:
                        reinas.pop()
                        tablero[fila][columna] = "-"
    else:
        return True    

def puede_colocar_reina(tablero, fila, columna, reinas):
    # Comprobar fila
    if "\x1b[31mX\x1b[m" in tablero[fila]:
        return False
    
    # Comprobar columna
    for i in reinas:
        if i[1] == columna:
            return False
        
    # Comprobar diagonal
    for i in reinas:
        if (i[1] - columna == i[0] - fila) or (i[1] - columna == -(i[0] - fila)):
            return False
    
    return True

#-----------------------------------------------------------------------------------------------------------------------

colocar_reina(tablero, reinas)
