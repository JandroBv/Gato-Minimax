import random
tablero = [	[1, "|",2,"|", 3],
			["-", "-","-","-", "-"],
			[4, "|",5,"|", 6],
			["-", "-","-","-", "-"],
			[7, "|",8,"|", 9]]

#IMPRIMIR TABLERO
def mostrarTablero(tablero):
		fila = 0
		columna = 0
		for i in range(0,25):
			print(tablero[fila][columna],end= '   ')
			columna += 1
			if columna == 5:
				columna = 0
				fila += 1
				print("\n")

#COLOCAR PIEZA EN EL TABLERO
def colocarPieza(posicion, jugador):
	fila = 0
	columna = 0
	for i in range(0,25):
		if columna == 5:
			fila += 1
			columna = 0
		if tablero[fila][columna] == posicion:
			tablero[fila][columna] = jugador
			break;
		columna += 1

#VERIFICAR SI EL JUGADOR INGRESADO COMO PARAMETRO HA GANADO
def ganador(jugador):
	for i in range(0, 5, 2):
		if tablero[i][0] == tablero[i][2] == tablero[i][4] == jugador or tablero[0][i] == tablero[2][i] == tablero[4][i] == jugador:
			return True
	if tablero[0][0] == tablero[2][2] == tablero[4][4] == jugador or tablero[0][4] == tablero[2][2] == tablero[4][0] == jugador:
		return True
	return False

#VER LA CANTIDAD DE LUGARES DISPONIBLES EN EL TABLERO
def NolugaresDisponibles():
	lugares = 0
	fila = 0
	columna = 0
	for i in range(25):
		if fila == 5:
			fila = 0
			columna += 1
		if tablero[fila][columna] in range(10):
			lugares +=1
		fila += 1
	return lugares

#VER LOS LUGARES DISPONIBLES EN EL TABLERO
def lugaresDisponibles():
	lugares = []
	fila = 0
	columna = 0
	for i in range(25):
		if columna == 5:
			columna = 0
			fila += 1
		if tablero[fila][columna] in range(10):
			lugares.append([tablero[fila][columna], [fila,columna]])
		columna += 1
	return lugares

#VERIFICAR SI UNA POSICION ES VALIDA
def posicionValida(posicion):
	fila = 0
	columna = 0
	for i in range(25):
		if fila == 5:
			fila = 0
			columna += 1
		if posicion == tablero[fila][columna]:
			return True
			break;
		fila += 1
	return False

#ALGORITMO DE MINIMAX
def minimax(jugador):
	pc = "O"
	jugador2 = "X" if jugador == "O" else "O"
	
	if ganador(jugador2):
		return {'posicion': None, 'puntuacion': 1 * (NolugaresDisponibles()+1) if jugador2 == pc else -1*(NolugaresDisponibles()+1)} 
	elif NolugaresDisponibles() == 0:
		return {'posicion': None, 'puntuacion': 0}
	
	if jugador == pc:
		mejor_resultado = {'posicion': None, 'puntuacion': -999}
	else:
		mejor_resultado = {'posicion': None, 'puntuacion': 999}
	
	for movimiento, posicion in lugaresDisponibles():
		colocarPieza(movimiento, jugador)
		resultado = minimax(jugador2)
		tablero[posicion[0]][posicion[1]] = movimiento
		resultado['posicion'] = movimiento

		if jugador == pc:
			if resultado['puntuacion'] > mejor_resultado['puntuacion']:
				mejor_resultado = resultado
		else:
			if resultado['puntuacion'] < mejor_resultado['puntuacion']:
				mejor_resultado = resultado
	return mejor_resultado

#REGRESA LA POSICION A LA QUE SE VA A MOVER LA COMPUTADORA
def turnoComputadora():
	posicion = 0
	pieza = "O"
	posicion = minimax(pieza)['posicion']
	return posicion

#INICIO DE JUEGO
def juego():
	jugador1 = "X"
	jugador2 = "O"
	turno = 1
	while ganador(jugador1) == False == ganador(jugador2) and NolugaresDisponibles() > 0:
		mostrarTablero(tablero)
		if turno == 1:
			jugador = int(input("Turno de X, ingresa la posicion a mover "))
			colocarPieza(jugador, jugador1)
			turno = 2
		else:
			print("Turno de la computadora...")
			colocarPieza(turnoComputadora(), jugador2)
			turno = 1
		print("---------------------------------------------------")
	mostrarTablero(tablero)
	if ganador(jugador1):
		print("El ganador es X")
	elif ganador(jugador2):
		print("El ganador es O")
	elif ganador(jugador1) == False == ganador(jugador2):
		print("Ha sido un empate")

juego()