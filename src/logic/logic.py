class Logica:

    def AND(self, a, b):
        """
        Implementa la operación lógica AND.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a AND b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        return a and b
    
    def OR(self, a, b):
        """
        Implementa la operación lógica OR.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a OR b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = a or b
        print(f"Resultado de {a} OR {b} es: {resultado}")
        return resultado
    
    def NOT(self, a):
        """
        Implementa la operación lógica NOT.
        
        Args:
            a (bool): Valor booleano
            
        Returns:
            bool: Resultado de NOT a
        """
        a = input("Ingrese un valor (True/False): ")
        
        a = a.strip().lower() == "true"
        
        resultado = not a
        print(f"Resultado de NOT {a} es: {resultado}")
        return resultado
    
    def XOR(self, a, b):
        """
        Implementa la operación lógica XOR (OR exclusivo).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XOR b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = (a and not b) or (not a and b)
        print(f"Resultado de {a} XOR {b} es: {resultado}")
        return resultado
    
    def NAND(self, a, b):
        """
        Implementa la operación lógica NAND (NOT AND).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NAND b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = not (a and b)
        print(f"Resultado de {a} NAND {b} es: {resultado}")
        return resultado
    
    def NOR(self, a, b):
        """
        Implementa la operación lógica NOR (NOT OR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NOR b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = not (a or b)
        print(f"Resultado de {a} NOR {b} es: {resultado}")
        return resultado
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        a = input("Ingrese el primer valor (True/False): ")
        b = input("Ingrese el segundo valor (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = (a and b) or (not a and not b)
        print(f"Resultado de {a} XNOR {b} es: {resultado}")
        return resultado
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        a = input("Ingrese el antecedente (a) (True/False): ")
        b = input("Ingrese el consecuente (b) (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = (not a) or b
        print(f"Resultado de {a} -> {b} es: {resultado}")
        return resultado
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        a = input("Ingrese el primer valor (a) (True/False): ")
        b = input("Ingrese el segundo valor (b) (True/False): ")

        a = a.strip().lower() == "true"
        b = b.strip().lower() == "true"

        resultado = (a and b) or (not a and not b)
        print(f"Resultado de {a} <-> {b} es: {resultado}")
        return resultado

log = Logica()

#AND
resultado = log.AND()
print("Resultado:", resultado)

#OR
log.OR()

#NOT
log.NOT()

#XOR
log.XOR()

#NAND
log.NAND()

#NOR
log.NOR()

#XNOR
log.XNOR()

#Implicacion
log.implicacion()

#Bi-Implicacion
log.bi_implicacion()
