class Magic:
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        n = int(input("Ingrese la posición n en la secuencia de Fibonacci: "))

        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        print(f"El número de Fibonacci en la posición {n} es: {b}")
        return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        n = int(input("Ingrese la cantidad de números a generar en la secuencia de Fibonacci: "))

        if n <= 0:
            print("Debe ingresar un número mayor a 0.")
            return []

        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])

        print(f"Los primeros {n} números de Fibonacci son: {fib}")
        return fib
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        n = int(input("Ingrese un número entero para verificar si es primo: "))

        if n < 2:
            print(f"{n} no es primo.")
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} no es primo.")
                return False

        print(f"{n} es primo.")
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        n = int(input("Ingrese el límite superior para generar números primos: "))

        primos = []
        for num in range(2, n + 1):
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)

        print(f"Números primos hasta {n}: {primos}")
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        n = int(input("Ingrese un número entero para verificar si es perfecto: "))

        if n < 1:
            print(f"{n} no es un número perfecto.")
            return False

        suma_divisores = 0
        for i in range(1, n):
            if n % i == 0:
                suma_divisores += i

        if suma_divisores == n:
            print(f"{n} es un número perfecto.")
            return True
        else:
            print(f"{n} no es un número perfecto.")
            return False
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        filas = int(input("Ingrese el número de filas del triángulo de Pascal: "))

        if filas <= 0:
            print("Debe ingresar un número mayor a 0.")
            return []

        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)
            triangulo.append(fila)

        print("Triángulo de Pascal:")
        for fila in triangulo:
            print(fila)
        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        n = int(input("Ingrese un número entero para calcular su factorial: "))

        if n < 0:
            print("No se puede calcular el factorial de un número negativo.")
            return None

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i

        print(f"El factorial de {n} es: {resultado}")
        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        # Algoritmo de Euclides
        x, y = a, b
        while y != 0:
            x, y = y, x % y

        print(f"El MCD de {a} y {b} es: {x}")
        return x

    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        x, y = a, b
        while y != 0:
            x, y = y, x % y
        mcd = x

        mcm = abs(a * b) // mcd

        print(f"El MCM de {a} y {b} es: {mcm}")
        return mcm

    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        n = int(input("Ingrese un número entero para sumar sus dígitos: "))
        suma = 0
        for digito in str(abs(n)):
            suma += int(digito)

        print(f"La suma de los dígitos de {n} es: {suma}")
        return suma

    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        n = int(input("Ingrese un número entero para verificar si es Armstrong: "))
        num_str = str(abs(n))
        num_digitos = len(num_str)
        suma = sum(int(digito) ** num_digitos for digito in num_str)

        if suma == n:
            print(f"{n} es un número de Armstrong.")
            return True
        else:
            print(f"{n} no es un número de Armstrong.")
            return False
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))
        matriz = []

        print("Ingrese los elementos de la matriz fila por fila:")
        for i in range(n):
            fila = []
            for j in range(n):
                valor = int(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(valor)
            matriz.append(fila)

        suma_ref = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_ref:
                print("No es un cuadrado mágico.")
                return False

        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_ref:
                print("No es un cuadrado mágico.")
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_ref or sum(matriz[i][n-1-i] for i in range(n)) != suma_ref:
            print("No es un cuadrado mágico.")
            return False

        print("Es un cuadrado mágico.")
        return True

magic = Magic()
    
#Fibonacci
magic.fibonacci()

#Secuencia Fibonacci
magic.secuencia_fibonacci()

#Es Primo
magic.es_primo()

#Generar Primos
magic.generar_primos()

#Es Numero Perfecto
magic.es_numero_perfecto()

#Triangulo Pascal
magic.triangulo_pascal()

#Factorial
magic.factorial()

# MCD
magic.mcd()

#MCM
magic.mcm()

#Suma Digitos
magic.suma_digitos()

#Es Numero Armstrong
magic.es_numero_armstrong()

#Es Cuadro Magico
magic.es_cuadrado_magico()