class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        # Empate
        if jugador1 == jugador2:
            return "empate"

        # Reglas
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "tijera" and jugador2 == "papel") or \
           (jugador1 == "papel" and jugador2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]

        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    def jugar_ta_te_ti(self):
        """
        Permite jugar Ta-Te-Ti por teclado entre dos jugadores.
        """
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        turno = "X"

        def imprimir_tablero():
            for fila in tablero:
                print(" | ".join(fila))
                print("-" * 5)

        print("Bienvenido a Ta-Te-Ti (Tic-Tac-Toe)")
        imprimir_tablero()

        while True:
            print(f"\nTurno de {turno}")
            fila = int(input("Ingresa la fila (0, 1, 2): "))
            col = int(input("Ingresa la columna (0, 1, 2): "))

            if tablero[fila][col] != " ":
                print("Esa posición ya está ocupada, intenta otra.")
                continue

            tablero[fila][col] = turno
            imprimir_tablero()

            estado = self.ta_te_ti_ganador(tablero)
            if estado == "X" or estado == "O":
                print(f"🎉 ¡Jugador {estado} gana!")
                break
            elif estado == "empate":
                print("🤝 ¡Empate!")
                break

            turno = "O" if turno == "X" else "X"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        print(f"🎲 Elige {longitud} colores de esta lista: {colores_disponibles}")
        combinacion = []
        for i in range(longitud):
            color = input(f"Ingrese color {i+1}: ").strip().lower()
            while color not in colores_disponibles:
                print("Color no válido. Intenta otra vez.")
                color = input(f"Ingrese color {i+1}: ").strip().lower()
            combinacion.append(color)
        print("\n" * 50) 
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False

        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True

tablero = [[" " for _ in range(8)] for _ in range(8)]

tablero[0][0] = "T"

juego = Games()

#Piedra, Papel o Tijera
j1 = input("Jugador 1, elige (piedra, papel o tijera): ")
j2 = input("Jugador 2, elige (piedra, papel o tijera): ")

resultado = juego.piedra_papel_tijera(j1, j2)
print("Resultado:", resultado)

#Adivinar Numero Pista
numero_secreto = int(input("Jugador 1, ingresa el número secreto: "))
print("\n" * 50)  

print("🎲 Jugador 2, intenta adivinar el número")

intento = None
while intento != numero_secreto:
    intento = int(input("👉 Ingresa tu intento: "))
    pista = juego.adivinar_numero_pista(numero_secreto, intento)
    print("Resultado:", pista)

print("🎉 ¡Felicidades, lo adivinaste!")

#Ta Te Ti Ganador
juego.jugar_ta_te_ti()

#Generar Combinacion Mastermind
print("Combinación secreta:", juego.generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]))

#Validar Movimiento Torre Ajedrez
while True:
    print("\n--- Movimiento Torre ---")
    print("Ejemplo: fila y columna de 0 a 7")
    print("Torre actual en (0,0)\n")

    try:
        desde_fila = int(input("Fila inicial: "))
        desde_col = int(input("Columna inicial: "))
        hasta_fila = int(input("Fila destino: "))
        hasta_col = int(input("Columna destino: "))

        valido = juego.validar_movimiento_torre_ajedrez(desde_fila, desde_col, hasta_fila, hasta_col, tablero)

        if valido:
            print("✅ Movimiento válido")
        else:
            print("❌ Movimiento inválido")

    except ValueError:
        print("⚠️ Ingrese solo números entre 0 y 7.")

    salir = input("\n¿Quieres probar otro movimiento? (s/n): ").lower()
    if salir == "n":
        break
