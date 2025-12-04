# Ejemplos de Codigo - Grafos

class Grafo:
    """Clase para representar un grafo no dirigido"""
    
    def __init__(self):
        self.adyacencia = {}
    
    def agregar_vertice(self, v):
        """Agrega un vertice al grafo"""
        if v not in self.adyacencia:
            self.adyacencia[v] = []
    
    def agregar_arista(self, u, v):
        """Agrega una arista entre u y v"""
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        if v not in self.adyacencia[u]:
            self.adyacencia[u].append(v)
        if u not in self.adyacencia[v]:
            self.adyacencia[v].append(u)
    
    def obtener_adyacentes(self, v):
        """Retorna los vertices adyacentes a v"""
        return self.adyacencia.get(v, [])


# DFS - Busqueda en Profundidad

def dfs(grafo, inicio, visitados=None):
    """
    Busqueda en profundidad (Depth-First Search)
    Complejidad: O(V + E)
    """
    if visitados is None:
        visitados = set()
    
    visitados.add(inicio)
    print(f"Visitando: {inicio}")
    
    for adyacente in grafo.get(inicio, []):
        if adyacente not in visitados:
            dfs(grafo, adyacente, visitados)
    
    return visitados


# BFS - Busqueda en Amplitud

from collections import deque

def bfs(grafo, inicio):
    """
    Busqueda en amplitud (Breadth-First Search)
    Complejidad: O(V + E)
    """
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    resultado = []
    
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        print(f"Visitando: {nodo}")
        
        for adyacente in grafo.get(nodo, []):
            if adyacente not in visitados:
                visitados.add(adyacente)
                cola.append(adyacente)
    
    return resultado


# Algoritmo de Dijkstra

import heapq
from collections import defaultdict

def dijkstra(grafo_ponderado, inicio):
    """
    Algoritmo de Dijkstra - Camino mas corto
    Complejidad: O((V + E) log V)
    """
    distancias = defaultdict(lambda: float('inf'))
    distancias[inicio] = 0
    
    cola_prioridad = [(0, inicio)]
    visitados = set()
    
    while cola_prioridad:
        dist_actual, nodo = heapq.heappop(cola_prioridad)
        
        if nodo in visitados:
            continue
        
        visitados.add(nodo)
        
        for adyacente, peso in grafo_ponderado.get(nodo, []):
            distancia_nueva = dist_actual + peso
            
            if distancia_nueva < distancias[adyacente]:
                distancias[adyacente] = distancia_nueva
                heapq.heappush(cola_prioridad, (distancia_nueva, adyacente))
    
    return distancias


# Detectar Componentes Conexas

def encontrar_componentes_conexas(grafo):
    """
    Encuentra todas las componentes conexas del grafo
    """
    visitados = set()
    componentes = []
    
    def dfs_componente(nodo, componente):
        visitados.add(nodo)
        componente.append(nodo)
        
        for adyacente in grafo.get(nodo, []):
            if adyacente not in visitados:
                dfs_componente(adyacente, componente)
    
    for nodo in grafo:
        if nodo not in visitados:
            componente = []
            dfs_componente(nodo, componente)
            componentes.append(componente)
    
    return componentes


# Detectar Ciclos

def tiene_ciclo(grafo):
    """Detecta si el grafo contiene ciclos"""
    visitados = set()
    rec_stack = set()
    
    def dfs_ciclo(nodo, padre=None):
        visitados.add(nodo)
        rec_stack.add(nodo)
        
        for adyacente in grafo.get(nodo, []):
            if adyacente not in visitados:
                if dfs_ciclo(adyacente, nodo):
                    return True
            elif adyacente != padre and adyacente in rec_stack:
                return True
        
        rec_stack.remove(nodo)
        return False
    
    for nodo in grafo:
        if nodo not in visitados:
            if dfs_ciclo(nodo):
                return True
    
    return False


# Matriz de Adyacencia

class GrafoMatriz:
    """Representacion de grafo usando matriz de adyacencia"""
    
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}
        self.indice_vertice = {}
    
    def agregar_vertice(self, v):
        if v not in self.vertices:
            idx = len(self.vertices)
            self.vertices[v] = idx
            self.indice_vertice[idx] = v
    
    def agregar_arista(self, u, v, peso=1):
        idx_u = self.vertices[u]
        idx_v = self.vertices[v]
        self.matriz[idx_u][idx_v] = peso
        self.matriz[idx_v][idx_u] = peso
    
    def obtener_matriz(self):
        return self.matriz
    
    def imprimir_matriz(self):
        vertices = list(self.vertices.keys())
        print("   ", "  ".join(vertices))
        for i, fila in enumerate(self.matriz[:len(vertices)]):
            print(f"{vertices[i]} {fila[:len(vertices)]}")


# === EJEMPLOS DE USO ===

if __name__ == "__main__":
    # Ejemplo 1: Grafo basico
    print("=== EJEMPLO 1: Grafo Basico ===")
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    print("\nDFS desde A:")
    dfs(grafo, 'A')
    
    print("\nBFS desde A:")
    resultado = bfs(grafo, 'A')
    print(f"Orden de visita: {resultado}")
    
    # Ejemplo 2: Dijkstra
    print("\n=== EJEMPLO 2: Algoritmo de Dijkstra ===")
    grafo_ponderado = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 5)],
        'C': [('A', 2), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    print("\nDistancias mas cortas desde A:")
    distancias = dijkstra(grafo_ponderado, 'A')
    for nodo, dist in sorted(distancias.items()):
        print(f"A -> {nodo}: {dist}")
    
    # Ejemplo 3: Componentes conexas
    print("\n=== EJEMPLO 3: Componentes Conexas ===")
    grafo_desconectado = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C', 'E'],
        'E': ['D'],
        'F': []
    }
    
    print("\nComponentes conexas:")
    componentes = encontrar_componentes_conexas(grafo_desconectado)
    for i, comp in enumerate(componentes, 1):
        print(f"Componente {i}: {comp}")
    
    # Ejemplo 4: Detectar ciclos
    print("\n=== EJEMPLO 4: Detectar Ciclos ===")
    grafo_con_ciclo = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['A']
    }
    
    print(f"¿El grafo tiene ciclos?: {tiene_ciclo(grafo_con_ciclo)}")
