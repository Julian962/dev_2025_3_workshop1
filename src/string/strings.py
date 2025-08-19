class Strings:
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = input("Ingrese un texto: ")
        texto_limpio = ''.join(texto.lower().split())
        es_palindromo = texto_limpio == texto_limpio[::-1]

        if es_palindromo:
            print("Es un palíndromo.")
        else:
            print("No es un palíndromo.")

        return es_palindromo
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        texto = input("Ingrese un texto: ")
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida  
        print(f"Cadena invertida: {invertida}")
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        texto = input("Ingrese un texto: ")
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1

        print(f"Número de vocales: {contador}")
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        texto = input("Ingrese un texto: ")
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1

        print(f"Número de consonantes: {contador}")
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1 = input("Ingrese la primera cadena: ").replace(" ", "").lower()
        texto2 = input("Ingrese la segunda cadena: ").replace(" ", "").lower()

        def contar_caracteres(texto):
            conteo = {}
            for c in texto:
                if c in conteo:
                    conteo[c] += 1
                else:
                    conteo[c] = 1
            return conteo

        es_anagrama = contar_caracteres(texto1) == contar_caracteres(texto2)

        if es_anagrama:
            print("Son anagramas.")
        else:
            print("No son anagramas.")

        return es_anagrama

    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        texto = input("Ingrese un texto: ")
        palabras = [palabra for palabra in texto.split(" ") if palabra != ""]
        cantidad = len(palabras)
        print(f"Número de palabras: {cantidad}")
        return cantidad
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        texto = input("Ingrese un texto: ")
        palabras = texto.split()
        resultado = ""
        for palabra in palabras:
            if palabra:
                resultado += palabra[0].upper() + palabra[1:] + " "
        resultado = resultado.strip()
        print(f"Texto formateado: {resultado}")
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        texto = input("Ingrese un texto: ")
        palabras = texto.split()  
        resultado = " ".join(palabras)
        print(f"Texto sin espacios duplicados: {resultado}")
        return resultado
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        texto = input("Ingrese un número entero: ").strip()
        if texto == "":
            print("No es un número entero.")
            return False

        if texto[0] in ("+", "-"):
            texto = texto[1:]

        es_entero = all(c in "0123456789" for c in texto) and texto != ""
        if es_entero:
            print("Es un número entero.")
        else:
            print("No es un número entero.")
        return es_entero
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        texto = input("Ingrese el texto a cifrar: ")
        desplazamiento_str = input("Ingrese el desplazamiento (entero): ")

        try:
            desplazamiento = int(desplazamiento_str)
        except ValueError:
            print("Desplazamiento no válido, se usará 0")
            desplazamiento = 0

        resultado = ""
        for char in texto:
            if 'a' <= char <= 'z':
                resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                resultado += char  
        print(f"Texto cifrado: {resultado}")
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        texto = input("Ingrese el texto a descifrar: ")
        desplazamiento_str = input("Ingrese el desplazamiento (entero): ")

        try:
            desplazamiento = int(desplazamiento_str)
        except ValueError:
            print("Desplazamiento no válido, se usará 0")
            desplazamiento = 0

        resultado = ""
        for char in texto:
            if 'a' <= char <= 'z':
                resultado += chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                resultado += chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A'))
            else:
                resultado += char  

        print(f"Texto descifrado: {resultado}")
        return resultado

    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        texto = input("Ingrese el texto principal: ")
        subcadena = input("Ingrese la subcadena a buscar: ")

        posiciones = []
        len_sub = len(subcadena)
        len_texto = len(texto)

        for i in range(len_texto - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)

        print(f"Posiciones encontradas: {posiciones}")
        return posiciones

strings = Strings()

#Es Palindromo
strings.es_palindromo()

#Invertir Cadena
strings.invertir_cadena()

#Contar Vocales
strings.contar_vocales()

#Contar Consonantes
strings.contar_consonantes()

#Es Anagrama
strings.es_anagrama()

#Contar Palabras
strings.contar_palabras()

#Palabras Mayus
strings.palabras_mayus()

#Eliminar Espacios Duplicados
strings.eliminar_espacios_duplicados()

#Es Numero Entero
strings.es_numero_entero()

#Cifrar Cesar
strings.cifrar_cesar()

#Descifrar Cesar
strings.descifrar_cesar()

#Encontrar Subcadena
strings.encontrar_subcadena()