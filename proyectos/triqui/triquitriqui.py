filas = 3
columnas = 3
tablero = [
    ["-" for _ in range(columnas)]
    for _ in range(filas)
]

jugadas_totales = filas * columnas
jugadas = 0
partida_ganada = False
jugador = "X"

while jugadas < jugadas_totales and not partida_ganada:
    print("\n    0    1    2")

    for fila_i in range(len(tablero)):
        print(f"{fila_i} {tablero[fila_i]}")

    print(f"JUGADOR {jugador}: ingrese fila y columna para jugar")
    jugada = input("fila columna: ").split()

    fila_jugada = int(jugada[0])
    columna_jugada = int(jugada[1])

    if tablero[fila_jugada][columna_jugada] == "-":
        tablero[fila_jugada][columna_jugada] = jugador
        jugadas += 1

        for i in range(filas):
            if all(tablero[i][j] == jugador for j in range(columnas)):
                partida_ganada = True

        for j in range(columnas):
            if all(tablero[i][j] == jugador for i in range(filas)):
                partida_ganada = True

        if all(tablero[i][i] == jugador for i in range(filas)):
            partida_ganada = True

        if all(tablero[i][filas - 1 - i] == jugador for i in range(filas)):
            partida_ganada = True

        if partida_ganada:
            print(f"¡EL JUGADOR {jugador} HA GANADO!")
        else:
            jugador = "X" if jugador == "O" else "O"
    else:
        print("Lugar ocupado, intente de nuevo")

    for fila in tablero:
        print(fila)

if not partida_ganada:
    print("¡EMPATE! No hay más espacios disponibles.")
