class Data:
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                print(f"Elemento '{elemento}' encontrado en la posición {i}")
                return i
        print(f"Elemento '{elemento}' no encontrado en la lista")
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        resultado = []
        for elemento in lista:
            if elemento not in resultado:
                resultado.append(elemento)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        i, j = 0, 0
        resultado = []

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return []

        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        stack = []

        def push(item):
            [].append(item)

        def pop():
            if not is_empty():
                return stack.pop()
            return "La pila está vacía"

        def peek():
            if not is_empty():
                return stack[-1]
            return "La pila está vacía"

        def is_empty():
            return len(stack) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def enqueue(item):
            cola.append(item)
            print(f"Se agregó {item} a la cola.")

        def dequeue():
            if not is_empty():
                item = cola.pop(0)
                print(f"Se eliminó {item} de la cola.")
                return item
            else:
                print("La cola está vacía.")

        def peek():
            if not is_empty():
                print(f"El primer elemento en la cola es: {cola[0]}")
                return cola[0]
            else:
                print("La cola está vacía.")

        def is_empty():
            return len(cola) == 0

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty, "cola": cola}



    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        matriz = []

        print("Ingrese los elementos de la matriz:")
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = int(input(f"Elemento [{i + 1}][{j + 1}]: "))
                fila.append(valor)
            matriz.append(fila)

        transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

        return transpuesta

d = Data()
#Invertir Lista
print(d.invertir_lista([1, 2, 3, 4]))

#Buscar Elemento
d.buscar_elemento([10, 20, 30, 40], 30) 
d.buscar_elemento([10, 20, 30, 40], 50) 

#Eliminar Duplicados
entrada = input("Ingrese los elementos de la lista separados por espacio: ")
lista = entrada.split()
print("Lista sin duplicados:", d.eliminar_duplicados(lista))

#Merge Ordenado
entrada1 = input("Ingrese la primera lista ORDENADA (ej: 1 3 5): ")
entrada2 = input("Ingrese la segunda lista ORDENADA (ej: 2 4 6): ")

lista1 = list(map(int, entrada1.split())) if entrada1.strip() else []
lista2 = list(map(int, entrada2.split())) if entrada2.strip() else []

print("Lista combinada y ordenada:", d.merge_ordenado(lista1, lista2))

#Rotar Lista
entrada_lista = input("Ingrese los elementos de la lista separados por espacio: ")
lista = entrada_lista.split()  # Permite números o texto
k = int(input("Ingrese el número de posiciones a rotar: "))

print("Lista rotada:", d.rotar_lista(lista, k))

#Encuentra Numero Faltante
entrada = input("Ingrese los números de la lista separados por espacio (del 1 al n, con uno faltante): ")
lista = list(map(int, entrada.split()))

print("El número faltante es:", d.encuentra_numero_faltante(lista))

#Es Subconjunto
entrada1 = input("Ingrese los elementos del primer conjunto separados por espacio: ")
entrada2 = input("Ingrese los elementos del segundo conjunto separados por espacio: ")

conjunto1 = entrada1.split()
conjunto2 = entrada2.split()

print("¿El primer conjunto es subconjunto del segundo?:", d.es_subconjunto(conjunto1, conjunto2))

#Implementar Pila
pila = d.implementar_pila()

while True:
    print("\n--- Menú Pila ---")
    print("1. Push (agregar)")
    print("2. Pop (quitar)")
    print("3. Peek (ver tope)")
    print("4. ¿Está vacía?")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = input("Ingrese un valor para apilar: ")
        pila["push"](valor)
        print(f"Se agregó '{valor}' a la pila")

    elif opcion == "2":
        print("Elemento desapilado:", pila["pop"]())

    elif opcion == "3":
        print("Tope de la pila:", pila["peek"]())

    elif opcion == "4":
        print("¿La pila está vacía?:", pila["is_empty"]())

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

#Iplementar Cola
    cola_obj = d.implementar_cola()  
while True:
    print("\n--- MENÚ COLA ---")
    print("1. Enqueue (Agregar)")
    print("2. Dequeue (Eliminar)")
    print("3. Peek (Ver primero)")
    print("4. Mostrar cola")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        item = input("Ingrese el elemento a agregar: ")
        cola_obj["enqueue"](item)
    elif opcion == "2":
        cola_obj["dequeue"]()
    elif opcion == "3":
        cola_obj["peek"]()
    elif opcion == "4":
        print("Cola actual:", cola_obj["cola"])
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente nuevamente.")

#Matriz Transpuesta
resultado = d.matriz_transpuesta()
print("Matriz transpuesta:")
for fila in resultado:
    print(fila)

