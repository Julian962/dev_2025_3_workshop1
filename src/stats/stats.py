class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular el promedio de una lista vacía.")
            return None

        media = sum(numeros) / n
        print(f"La media aritmética es: {media}")
        return media
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular la mediana de una lista vacía.")
            return None

        numeros.sort()
        mitad = n // 2

        if n % 2 == 0:
            mediana = (numeros[mitad - 1] + numeros[mitad]) / 2
        else:
            mediana = numeros[mitad]

        print(f"La mediana es: {mediana}")
        return mediana
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular la moda de una lista vacía.")
            return None

        frecuencia = {}
        for num in numeros:
            frecuencia[num] = frecuencia.get(num, 0) + 1

        moda = max(frecuencia, key=frecuencia.get)
        print(f"La moda es: {moda}")
        return moda

    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular la desviación estándar de una lista vacía.")
            return None

        media = sum(numeros) / n
        varianza = sum((x - media) ** 2 for x in numeros) / n
        desviacion = varianza ** 0.5

        print(f"La desviación estándar es: {desviacion}")
        return desviacion
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular la varianza de una lista vacía.")
            return None

        media = sum(numeros) / n
        varianza = sum((x - media) ** 2 for x in numeros) / n

        print(f"La varianza es: {varianza}")
        return varianza
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            valor = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(valor)

        if n == 0:
            print("No se puede calcular el rango de una lista vacía.")
            return None

        rango_valor = max(numeros) - min(numeros)
        print(f"El rango es: {rango_valor}")
        return rango_valor

stats = Stats()

#Promedio
stats.promedio()

#Mediana
stats.mediana()

#Moda
stats.moda()

#Desviacion Estandar
stats.desviacion_estandar()

#Varianza
stats.varianza()

#Rango
stats.rango()