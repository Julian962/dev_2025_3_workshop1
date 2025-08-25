class Strings:
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ''.join(texto.lower().split())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = set("aeiouAEIOU")
        return sum(1 for c in texto if c in vocales)
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = set("aeiouAEIOU")
        return sum(1 for c in texto if c.isalpha() and c not in vocales)

    def es_anagrama(self, texto1, texto2):
        t1 = texto1.replace(" ", "").lower()
        t2 = texto2.replace(" ", "").lower()
        def contar_caracteres(t):
            d = {}
            for ch in t:
                d[ch] = d.get(ch, 0) + 1
            return d
        return contar_caracteres(t1) == contar_caracteres(t2)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        t1 = texto1.replace(" ", "").lower()
        t2 = texto2.replace(" ", "").lower()
        def contar_caracteres(t):
            d = {}
            for ch in t:
                d[ch] = d.get(ch, 0) + 1
            return d
        return contar_caracteres(t1) == contar_caracteres(t2)

    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        return len([p for p in texto.split(" ") if p != ""])
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        res = []
        nueva_palabra = True
        for ch in texto:
            if nueva_palabra and ch.isalpha():
                res.append(ch.upper())
                nueva_palabra = False
            else:
                res.append(ch)
                if ch.isalpha():
                    nueva_palabra = False
            if ch == ' ':
                nueva_palabra = True
        return ''.join(res)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        if texto == "":
            return ""
        had_leading = texto[0] == ' '
        had_trailing = texto[-1] == ' '
        collapsed = ' '.join(texto.split())
        if collapsed == "" and texto.strip() == "":
            return "" 
        if had_leading:
            collapsed = ' ' + collapsed
        if had_trailing:
            collapsed = collapsed + ' '
        return collapsed
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        s = texto.strip()
        if s == "":
            return False
        if s[0] in ("+", "-"):
            s = s[1:]
        return s != "" and all(ch in "0123456789" for ch in s)
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        try:
            k = int(desplazamiento)
        except (ValueError, TypeError):
            k = 0
        res = ""
        for ch in texto:
            if 'a' <= ch <= 'z':
                res += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            elif 'A' <= ch <= 'Z':
                res += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            else:
                res += ch
        return res
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        try:
            k = int(desplazamiento)
        except (ValueError, TypeError):
            k = 0
        return self.cifrar_cesar(texto, -k)

    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        n, m = len(texto), len(subcadena)
        if m == 0:
            return [] 
        for i in range(n - m + 1):
            if texto[i:i + m] == subcadena:
                posiciones.append(i)
        return posiciones