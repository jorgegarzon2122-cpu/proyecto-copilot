# Blog de Grafos - Estructura de Datos

## 📋 Descripción del Proyecto

Este es un blog educativo profesional sobre **Grafos** (Graphs), una de las estructuras de datos más fundamentales en informática. El proyecto contiene 3 artículos principales que cubren los aspectos esenciales de los grafos.

## 📚 Contenido del Blog

### Artículos Incluidos:

#### **Post #1: Introducción a los Grafos: Nodos, Aristas y Tipos**
- Definición formal de un grafo: G = (V, E)
- Conceptos clave: vértices/nodos, aristas/ejes
- Tipos de grafos: dirigidos, no dirigidos, ponderados
- Ejemplo visual de un grafo con 5 nodos
- Aplicaciones prácticas en el mundo real

#### **Post #2: Representación de Grafos**
- Matriz de Adyacencia
  - Funcionamiento y estructura
  - Ventajas y desventajas
  - Código Python de ejemplo
- Lista de Adyacencia
  - Funcionamiento y estructura
  - Ventajas y desventajas
  - Código Python de ejemplo
- Comparación directa entre ambas representaciones
- Tabla de complejidad computacional
- Recomendaciones sobre cuál usar según el contexto

#### **Post #3: Algoritmos Fundamentales de Recorrido: BFS y DFS**
- Búsqueda en Amplitud (BFS)
  - Explicación paso a paso
  - Ejemplo visual
  - Código Python completo
  - Aplicaciones prácticas
- Búsqueda en Profundidad (DFS)
  - Versión recursiva
  - Versión iterativa
  - Ejemplo visual
  - Código Python completo
  - Aplicaciones prácticas
- Comparación BFS vs DFS
- Cuándo usar cada algoritmo

## 🛠️ Tecnologías Utilizadas

- **HTML5**: Estructura del contenido
- **CSS3**: Diseño responsivo y profesional
- **JavaScript**: Funcionalidad interactiva
- **Python**: Ejemplos de código

## 📁 Estructura del Proyecto

```
blog/
├── index.html              # Página principal del blog
├── css/
│   └── style.css          # Estilos del blog
├── js/
│   └── main.js            # Funcionalidad JavaScript
├── posts/
│   ├── post1.html         # Post 1: Introducción a los Grafos
│   ├── post2.html         # Post 2: Representación de Grafos
│   └── post3.html         # Post 3: Algoritmos BFS y DFS
└── assets/                # Para futuras imágenes y recursos
```

## 🎨 Características de Diseño

- ✅ **Diseño Responsivo**: Funciona en desktop, tablet y móvil
- ✅ **Navegación Intuitiva**: Fácil movimiento entre posts
- ✅ **Estilos Profesionales**: Colores coherentes y tipografía legible
- ✅ **Diagrama ASCII**: Representaciones visuales de grafos
- ✅ **Código Formateado**: Ejemplos de Python con sintaxis clara
- ✅ **Tablas Comparativas**: Análisis de complejidad y opciones
- ✅ **Cajas de Información**: Destacados y consejos importantes

## 🚀 Cómo Usar

### Opción 1: Abrir Localmente
1. Descarga o clona el repositorio
2. Abre `blog/index.html` en tu navegador web
3. Navega entre los diferentes artículos

### Opción 2: Publicar en GitHub Pages
1. Sube el proyecto a GitHub
2. Ve a Settings → Pages
3. Selecciona la rama `main`
4. Tu blog estará disponible en: `https://tu-usuario.github.io/proyecto-copilot`

## 📖 Contenido Técnico

Cada artículo incluye:
- **Explicaciones claras** de conceptos complejos
- **Ejemplos visuales** con diagramas ASCII
- **Código Python** funcional y comentado
- **Tablas comparativas** para análisis
- **Aplicaciones prácticas** del mundo real
- **Recursos para aprender más**

## 📊 Cobertura de Contenido

### Conceptos Cubiertos:
- ✅ Definición formal de grafos
- ✅ Tipos de grafos (dirigidos, no dirigidos, ponderados)
- ✅ Componentes: vértices, aristas, pesos
- ✅ Matriz de adyacencia
- ✅ Lista de adyacencia
- ✅ Búsqueda en Amplitud (BFS)
- ✅ Búsqueda en Profundidad (DFS)
- ✅ Análisis de complejidad O(n)
- ✅ Aplicaciones reales

## 💻 Ejemplos de Código

Todos los ejemplos están en Python 3 y son completamente funcionales:

```python
# BFS Ejemplo
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    resultado = []
    
    while cola:
        vertice = cola.popleft()
        resultado.append(vertice)
        for adyacente in grafo[vertice]:
            if adyacente not in visitados:
                visitados.add(adyacente)
                cola.append(adyacente)
    
    return resultado
```

## 🎯 Objetivos Educativos

Al completar la lectura de estos artículos, serás capaz de:

1. **Comprender**: Qué son los grafos y sus componentes
2. **Diferenciar**: Los tipos de grafos y cuándo usar cada uno
3. **Implementar**: Ambas representaciones de grafos
4. **Aplicar**: BFS y DFS para recorrer grafos
5. **Analizar**: La complejidad de diferentes operaciones
6. **Evaluar**: Cuál representación o algoritmo es mejor según el contexto

## 🔗 Referencias y Recursos

- **Estructura de Datos**: Grafos fundamentales
- **Algoritmos Clásicos**: BFS y DFS
- **Análisis de Complejidad**: O(V + E)
- **Aplicaciones Prácticas**: Desde redes hasta navegación

## 📝 Requisitos

- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conocimiento básico de programación (para entender el código Python)
- Curiosidad por aprender estructuras de datos

## 🔄 Próximas Expansiones

Temas futuros a considerar:
- Algoritmos de camino más corto (Dijkstra)
- Árbol de expansión mínima (Prim, Kruskal)
- Detección de ciclos
- Componentes conexas
- Ordenamiento topológico

## 👨‍💻 Autor

**Jorge Garzon** - Proyecto educativo para Estructura de Datos 2

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo licencia educativa.

## 🔗 GitHub

Repositorio: [https://github.com/jorgegarzon2122-cpu/proyecto-copilot](https://github.com/jorgegarzon2122-cpu/proyecto-copilot)

---

**Última Actualización**: 3 de Diciembre, 2025

¡Gracias por leer el Blog de Grafos! 📊
