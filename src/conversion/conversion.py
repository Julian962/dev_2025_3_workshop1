class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return(celsius * 9/5) + 32

    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return(fahrenheit - 32) * 5/9
    
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        metros = 3.28084
        return(metros * Distancia)
    
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        pies = 0.3048
        return (pies * Distancia)
    
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        return(decimal)
    
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        return int(binario, 2)
    
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        miles = ["", "M", "MM", "MMM"]
        centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            miles[numero // 1000]+
            centenas[(numero % 1000)//100]+
            decenas[(numero % 100)//10]+
            unidades[numero % 10]
        )
    
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        valores = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        prev = 0
        for letra in romano.upper()[::-1]:  
            valor = valores[letra]
            if valor < prev:
                total -= valor
            else:
                total += valor
            prev = valor
        return total

    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }
        texto = texto.upper()
        return ' '.join(morse[char] for char in texto if char in morse)
    
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        morse = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
            '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9'
        }
        return ''.join(morse[char] for char in Codigo.split() if char in morse)
    
#Conversion para todas la Funciones
conv = Conversion()

#Celsius a Fahrenheit
Temperatura = float(input('Ingrese la Temperatura en Celsius: '))
Resultado = conv.celsius_a_fahrenheit(Temperatura)
print("La Temperatura en Fahrenheit es: ",Resultado)

#Celsius a Fahrenheit        
Temperatura = float(input('Ingrese la Temperatura en Fahrenheit: '))
Resultado = conv.fahrenheit_a_celsius(Temperatura)
print("La Temperatura en Celsius es: ",Resultado)

#Metros a Pies
Distancia = float(input('Ingrese la Distancia en Metros: '))
Resultado = conv.metros_a_pies(Distancia)
print("La Distancia en Pies es: ",Resultado)

#Pies a Metros
Distancia = float(input('Ingrese la Distancia en Pies: '))
Resultado = conv.pies_a_metros(Distancia)
print("La Distancia en Metros es: ",Resultado)

#Decimal a Binario
Cambio = int(input('Ingrese el número Decimal: '))
Resultado = conv.decimal_a_binario(Cambio)
Binario = bin(Resultado)[2:]
print('El número en Binario es: ',Binario)

#Binario a Decimal
Cambio = input('Ingrese el número Binario: ')
Resultado = conv.binario_a_decimal(Cambio)
print('El número en Decimal es: ',Resultado)

#Decimal a Romano
Numeros = int(input('Ingrese el número Decimal: '))
print("El número Romano es: ",conv.decimal_a_romano(Numeros))

#Romano a Decimal
Romano = input("Ingrese un número romano: ")
print("Número decimal:", conv.romano_a_decimal(Romano))

#Texto a Morse
Mensaje = input("Ingrese el texto: ")
print("Código Morse:", conv.texto_a_morse(Mensaje))

#Morse a Texto
Codigo = input("Ingrese el código Morse (separado por espacios): ")
print("Texto:", conv.morse_a_texto(Codigo))