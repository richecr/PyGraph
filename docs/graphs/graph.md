# [Grafo Base](https://github.com/Rickecr/PyGraph/blob/deb3fa4cb011f42255dd48ee4c54660205928af2/py_graph_t/Graph.py#L12)
Esse é o grafo que todos os outros grafos vão herdar suas características/métodos.

Esse grafo não possui nenhum tipo de restrição. Pois todos os outros grafos irão sobrescrever os métodos necessários para aplicar suas restrições.

## Métodos:

| Método | Parâmetros | O que faz ? | Retorno |
----------------- | ---------- | --------- |--------- |
| `add_vertex`       |   value    |  Método que adiciona um vértice ao grafo.       | SimpleVertex adicionado |
| `delete_vertex` | value | Método que remove um vertice do grafo e consequentemente todas as arestas conectadas ao vertice.  | SimpleVertex removido  |
| `add_edge`  | value_a, value_b, name(opcional)  | Método que adiciona uma aresta ao grafo.  | SimpleEdge adicionado. |
| `delete_edge`   | value_a, value_b  | Método que remove uma aresta do grafo.    | SimpleEdge removido.    |
| `show_edge` | value_a, value_b   | Método que retorna uma aresta entre dois vértices, se ela existe.  | SimpleEdge.  |
| `is_terminal`   | edge, value   | Método que verifica se um dado vértice é terminal de uma dada aresta.  | Boolean  |
| `num_vertex` | ---   | Método que retorna o número de vértices no grafo.  | Integer  |
| `num_edges` | ---   | Método que retorna o número de arestas no grafo.  | Integer  |
| `vertex_exists` | value   | Método que indica se um determinado vértice pertence ao Grafo.  | Boolean  |
| `edge_exists` | value_a, value_b   | Método que indica se uma determinada aresta pertence ao Grafo.  | Boolean  |
| `vertex_neighbors` | value   | Método que encontra vertices vizinhos do vertice de entrada.  | List  |
| `vertex_degree` | value   | Método que retorna o grau do vértice de entrada.  | Integer  |
| `is_vertices_adjacents` | value_a, value_b   | Método que indica se os vértices de entrada são adjacentes.  | Boolean  |
| `get_all_vertex` | ---   | Método que retorna uma lista com os vértices do grafo.  | List  |
| `list_graph_vertices` | ---   | Método que retorna lista com todos os identificadores dos vértices do grafo.  | List   |
| `list_graph_edges` | ---   | Método que retorna lista com todos os nomes as arestas do grafo.   | List  |
| `cycle` | v, visited, parent   | Método que verifica se tem ciclo no subgrafo a partir do vértice v.   | Boolean  |
| `has_cycle` | ---   | Método que verifica se o grafo possui um ciclo. Loops também são detectados.  | Boolean  |
| `has_loop` | ---   | Método que verifica se o grafo possui um loop.  | Boolean  |
| `check_regular_graph` | ---   | Método que verifica a regularidade de um grafo.  | Boolean  |
| `incidence_list` | ---   | Método que retorna uma lista de objetos que contem a incidencia dos vertices com as arestas.  | List<ValueBinding>  |
| `adjacency_matrix` | ---   | Método que retorna a representação em forma de matriz de adjacência do grafo.  | Dict  |
| `__str__` | ---   | Método que retorna a representação textual do grafo.  | String  |


## Exemplos de uso:
Não faz muito sentido ter um grafo como esse, ele existe na biblioteca apenas para servir para reuso.

### Grafo Base - Adicionar um vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_vertex("c")
~~~

### Grafo Base - Deletar um vértice

~~~python3
grafo = Graph()
grafo.delete_vertex("a")
grafo.delete_vertex("b")
grafo.delete_vertex("c")
~~~

### Grafo Base - Adicionar uma aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
~~~

### Grafo Base - Deletar uma aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
grafo.delete_edge("a", "a")
~~~

### Grafo Base - Visualizar aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
print(grafo.show_edge("a", "b"))
~~~

### Grafo Base - Verificar se um vértice é terminal de uma aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
edge = grafo.show_edge("a", "b")
grafo.is_terminal(edge, "b")
grafo.is_terminal(edge, "a")
~~~

### Grafo Base - Número de vértices

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.num_vertex())
~~~

### Grafo Base - Número de arestas

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.num_edges())
~~~

### Grafo Base - Verifica se um vértice existe

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.vertex_exists("a"))
~~~

### Grafo Base - Verifica se uma aresta existe

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
print(grafo.edge_exists("a", "b"))
~~~

### Grafo Base - Vizinhos de um vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.vertex_neighbors("a"))
~~~

### Grafo Base - Grau do vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.vertex_degree("a"))
~~~

### Grafo Base - Verifica se os vértices são adjacentes

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.is_vertices_adjacents("a", "b"))
~~~

### Grafo Base - Lista dos vértices do grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.get_all_vertex())
~~~

### Grafo Base - Lista com todos os identificadores dos vértices

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.list_graph_vertices())
~~~

### Grafo Base - Lista com os nomes das arestas

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.get_all_vertex())
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.list_graph_edges())
~~~

### Grafo Base - Verifica se um grafo possui ciclos, loops também são detectados

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.has_cycle())
~~~

### Grafo Base - Verifica se um grafo possui um loop

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.has_loop())
~~~

### Grafo Base - Verifica a regularidade de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.check_regular_graph())
~~~

### Grafo Base - Incidência de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.incidence_list())
~~~

### Grafo Base - Adjacência de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.adjacency_matrix())
~~~

### Grafo Base - Representação textual

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.__str__())
~~~
