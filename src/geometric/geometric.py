class Geometria:
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Área del rectángulo
        """
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        """
        Calcula el perímetro de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Perímetro del rectángulo
        """
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        
        perimetro = 2 * (base + altura)
        print(f"El perímetro del rectángulo es: {perimetro}")
        return perimetro
    
    def area_circulo(self, radio):
        """
        Calcula el área de un círculo.
        
        Args:
            radio (float): Radio del círculo
            
        Returns:
            float: Área del círculo
        """
        radio = float(input("Ingrese el radio del círculo: "))
        
        area = 3.1416 * (radio ** 2)
        
        return area
    
    def perimetro_circulo(self, radio):
        """
        Calcula el perímetro (circunferencia) de un círculo.
        
        Args:
            radio (float): Radio del círculo
            
        Returns:
            float: Perímetro del círculo
        """
        radio = float(input("Ingrese el radio del círculo: "))
        perimetro = 2 * 3.1416 * radio
        print(f"El perímetro del círculo es: {perimetro}")
        return perimetro
    
    def area_triangulo(self, base, altura):
        """
        Calcula el área de un triángulo.
        
        Args:
            base (float): Longitud de la base del triángulo
            altura (float): Altura del triángulo
            
        Returns:
            float: Área del triángulo
        """
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
     
        area = (base * altura) / 2
        
        print(f"El área del triángulo es: {area}")
        return area
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        """
        Calcula el perímetro de un triángulo.
        
        Args:
            lado1 (float): Longitud del primer lado
            lado2 (float): Longitud del segundo lado
            lado3 (float): Longitud del tercer lado
            
        Returns:
            float: Perímetro del triángulo
        """
        lado1 = float(input("Ingrese la longitud del primer lado: "))
        lado2 = float(input("Ingrese la longitud del segundo lado: "))
        lado3 = float(input("Ingrese la longitud del tercer lado: "))

        perimetro = lado1 + lado2 + lado3
        print(f"El perímetro del triángulo es: {perimetro}")
        return perimetro
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo válido.
        Un triángulo es válido si la suma de las longitudes de dos lados
        es mayor que la longitud del tercer lado, para todos los lados.
        
        Args:
            lado1 (float): Longitud del primer lado
            lado2 (float): Longitud del segundo lado
            lado3 (float): Longitud del tercer lado
            
        Returns:
            bool: True si los lados pueden formar un triángulo, False en caso contrario
        """
        lado1 = float(input("Ingrese la longitud del primer lado: "))
        lado2 = float(input("Ingrese la longitud del segundo lado: "))
        lado3 = float(input("Ingrese la longitud del tercer lado: "))

        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            print("Es un triángulo válido ✅")
            return True
        else:
            print("No es un triángulo válido ❌")
            return False
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        """
        Calcula el área de un trapecio.
        
        Args:
            base_mayor (float): Longitud de la base mayor
            base_menor (float): Longitud de la base menor
            altura (float): Altura del trapecio
            
        Returns:
            float: Área del trapecio
        """
        base_mayor = float(input("Ingrese la longitud de la base mayor: "))
        base_menor = float(input("Ingrese la longitud de la base menor: "))
        altura = float(input("Ingrese la altura del trapecio: "))

        area = ((base_mayor + base_menor) * altura) / 2
        print(f"El área del trapecio es: {area}")
        return area
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        """
        Calcula el área de un rombo usando sus diagonales.
        
        Args:
            diagonal_mayor (float): Longitud de la diagonal mayor
            diagonal_menor (float): Longitud de la diagonal menor
            
        Returns:
            float: Área del rombo
        """
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))

        area = (diagonal_mayor * diagonal_menor) / 2
        print(f"El área del rombo es: {area}")
        return area
    
    def area_pentagono_regular(self, lado, apotema):
        """
        Calcula el área de un pentágono regular.
        
        Args:
            lado (float): Longitud del lado del pentágono
            apotema (float): Longitud de la apotema (distancia del centro al punto medio de un lado)
            
        Returns:
            float: Área del pentágono regular
        """
        lado = float(input("Ingrese la longitud del lado del pentágono: "))
        apotema = float(input("Ingrese la longitud de la apotema: "))

        perimetro = 5 * lado
        area = (perimetro * apotema) / 2

        print(f"El área del pentágono regular es: {area}")
        return area
    
    def perimetro_pentagono_regular(self, lado):
        """
        Calcula el perímetro de un pentágono regular.
        
        Args:
            lado (float): Longitud del lado del pentágono
            
        Returns:
            float: Perímetro del pentágono regular
        """
        lado = float(input("Ingrese la longitud del lado del pentágono: "))
        perimetro = 5 * lado
        print(f"El perímetro del pentágono regular es: {perimetro}")
        return perimetro
    
    def area_hexagono_regular(self, lado, apotema):
        """
        Calcula el área de un hexágono regular.
        
        Args:
            lado (float): Longitud del lado del hexágono
            apotema (float): Longitud de la apotema (distancia del centro al punto medio de un lado)
            
        Returns:
            float: Área del hexágono regular
        """
        lado = float(input("Ingrese la longitud del lado del hexágono: "))
        apotema = float(input("Ingrese la longitud de la apotema del hexágono: "))
        perimetro = 6 * lado
        area = (perimetro * apotema) / 2

        print(f"El área del hexágono regular es: {area}")
        return area
    
    def perimetro_hexagono_regular(self, lado):
        """
        Calcula el perímetro de un hexágono regular.
        
        Args:
            lado (float): Longitud del lado del hexágono
            
        Returns:
            float: Perímetro del hexágono regular
        """
        lado = float(input("Ingrese la longitud del lado del hexágono: "))
        perimetro = 6 * lado
        return perimetro
    
    def volumen_cubo(self, lado):
        """
        Calcula el volumen de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Volumen del cubo
        """
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        volumen = lado ** 3
        print(f"El volumen del cubo es: {volumen}")
        return volumen
    
    def area_superficie_cubo(self, lado):
        """
        Calcula el área de la superficie de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Área de la superficie del cubo
        """
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        area = 6 * (lado ** 2)
        return area
    
    def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Volumen de la esfera
        """
        pi = 3.1416  
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen = (4/3) * pi * (radio ** 3)
        print(f"El volumen de la esfera es: {volumen}")
        return volumen
    
    def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Área de la superficie de la esfera
        """
        radio = float(input("Ingrese el radio de la esfera: "))
        area = 4 * 3.1416 * (radio ** 2)
        
        return area
    
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        radio = float(input("Ingrese el radio de la base del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))

        volumen = 3.1416 * (radio ** 2) * altura
        print(f"El volumen del cilindro es: {volumen}")
        return volumen
    
    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Área de la superficie del cilindro
        """
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        pi = 3.1416
        area = 2 * pi * radio * (altura + radio)
        
        print(f"El área de la superficie del cilindro es: {area}")
        return area
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Distancia entre los dos puntos
        """
        x1 = float(input("Ingrese la coordenada x1: "))
        y1 = float(input("Ingrese la coordenada y1: "))
        x2 = float(input("Ingrese la coordenada x2: "))
        y2 = float(input("Ingrese la coordenada y2: "))

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        print(f"La distancia entre los puntos es: {distancia}")
        return distancia
    
    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coordenadas (x, y) del punto medio
        """
        x1 = float(input("Ingrese la coordenada x1: "))
        y1 = float(input("Ingrese la coordenada y1: "))
        x2 = float(input("Ingrese la coordenada x2: "))
        y2 = float(input("Ingrese la coordenada y2: "))

        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

        print(f"El punto medio entre ({x1}, {y1}) y ({x2}, {y2}) es: ({xm}, {ym})")
        return (xm, ym)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Pendiente de la recta
        """
        x1 = float(input("Ingrese la coordenada x1: "))
        y1 = float(input("Ingrese la coordenada y1: "))
        x2 = float(input("Ingrese la coordenada x2: "))
        y2 = float(input("Ingrese la coordenada y2: "))

        if x2 == x1:
            print("La pendiente es indefinida (recta vertical).")
            return None
        else:
            pendiente = (y2 - y1) / (x2 - x1)
            print(f"La pendiente de la recta es: {pendiente}")
            return pendiente
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        x1 = float(input("Ingrese la coordenada x1: "))
        y1 = float(input("Ingrese la coordenada y1: "))
        x2 = float(input("Ingrese la coordenada x2: "))
        y2 = float(input("Ingrese la coordenada y2: "))

        A = y1 - y2
        B = x2 - x1
        C = (x1 * y2) - (x2 * y1)

        print(f"La ecuación de la recta es: {A}x + {B}y + {C} = 0")
        return (A, B, C)
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        num_lados = int(input("Ingrese el número de lados del polígono: "))
        lado = float(input("Ingrese la longitud de cada lado: "))
        apotema = float(input("Ingrese la longitud de la apotema: "))

        perimetro = num_lados * lado
        area = (perimetro * apotema) / 2

        print(f"El área del polígono regular es: {area}")
        return area
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        num_lados = int(input("Ingrese el número de lados del polígono: "))
        lado = float(input("Ingrese la longitud de cada lado: "))
        
        perimetro = num_lados * lado
        print(f"El perímetro del polígono regular es: {perimetro}")
        return perimetro

geo = Geometria()

#Area Rectangulo
area = geo.area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area}")

#Area de Circulo
print("El área del círculo es:", geo.area_circulo())

#Perimetro Circulo
geo.perimetro_circulo()

#Area de Triangulo
geo.area_triangulo()

#Perimetro Hexagono Regular
print("El perímetro del hexágono regular es:", geo.perimetro_hexagono_regular())

#Volumen Esfera
geo.volumen_esfera()

#Area Superficie Esfera
print("El área de la superficie es:", geo.area_superficie_esfera())

#Volumen Cilindro
geo.volumen_cilindro()

#Area Superficie Cilindro
geo.area_superficie_cilindro()

#Distancia Entre Puntos
geo.distancia_entre_puntos()

#Punto Medio
geo.punto_medio()

#Pendiente Recta
geo.pendiente_recta()

#Ecuacion Recta
geo.ecuacion_recta()

#Area Poligono Regular
geo.area_poligono_regular()


