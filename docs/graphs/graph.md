# [Grafo Base](https://github.com/Rickecr/PyGraph/blob/deb3fa4cb011f42255dd48ee4c54660205928af2/py_graph_t/Graph.py#L12)
Esse é o grafo que todos os outros grafos vão herdar suas características/métodos.

Esse grafo não possui nenhum tipo de restrição. Pois todos os outros grafos irão sobrescrever os métodos necessários para aplicar suas restrições.

## Métodos:

| Método | Parâmetros | O que faz ? | Retorno |
----------------- | ---------- | --------- |--------- |
| [add_vertex](#adicionar-um-vértice)       |   value    |  Método que adiciona um vértice ao grafo.       | SimpleVertex adicionado |
| [delete_vertex](#deletar-um-vértice) | value | Método que remove um vertice do grafo e consequentemente todas as arestas conectadas ao vertice.  | SimpleVertex removido  |
| [add_edge](#adicionar-uma-aresta)  | value_a, value_b, name(opcional)  | Método que adiciona uma aresta ao grafo.  | SimpleEdge adicionado. |
| [delete_edge](#deletar-uma-aresta)   | value_a, value_b  | Método que remove uma aresta do grafo.    | SimpleEdge removido.    |
| [show_edge](#visualizar-aresta) | value_a, value_b   | Método que retorna uma aresta entre dois vértices, se ela existe.  | SimpleEdge.  |
| [is_terminal](#verificar-se-um-vértice-é-terminal-de-uma-aresta)   | edge, value   | Método que verifica se um dado vértice é terminal de uma dada aresta.  | Boolean  |
| [num_vertex](#número-de-vértices) | ---   | Método que retorna o número de vértices no grafo.  | Integer  |
| [num_edges](#número-de-arestas) | ---   | Método que retorna o número de arestas no grafo.  | Integer  |
| [vertex_exists](#verifica-se-um-vértice-existe) | value   | Método que indica se um determinado vértice pertence ao Grafo.  | Boolean  |
| [edge_exists](#verifica-se-uma-aresta-existe) | value_a, value_b   | Método que indica se uma determinada aresta pertence ao Grafo.  | Boolean  |
| [vertex_neighbors](#vizinhos-de-um-vértice) | value   | Método que encontra vertices vizinhos do vertice de entrada.  | List  |
| [vertex_degree](#grau-do-vértice) | value   | Método que retorna o grau do vértice de entrada.  | Integer  |
| [is_vertices_adjacents](#verifica-se-os-vértices-são-adjacentes) | value_a, value_b   | Método que indica se os vértices de entrada são adjacentes.  | Boolean  |
| [get_all_vertex](#lista-dos-vértices-do-grafo) | ---   | Método que retorna uma lista com os vértices do grafo.  | List  |
| [list_graph_vertices](#lista-com-todos-os-identificadores-dos-vértices) | ---   | Método que retorna lista com todos os identificadores dos vértices do grafo.  | List   |
| [list_graph_edges](#lista-com-os-nomes-das-arestas) | ---   | Método que retorna lista com todos os nomes as arestas do grafo.   | List  |
|[cycle](#) | v, visited, parent   | Método que verifica se tem ciclo no subgrafo a partir do vértice v.   | Boolean  |
|[has_cycle](#verifica-se-um-grafo-possui-ciclos-loops-também-são-detectados) | ---   | Método que verifica se o grafo possui um ciclo. Loops também são detectados.  | Boolean  |
|[has_loop](#verifica-se-um-grafo-possui-um-loop) | ---   | Método que verifica se o grafo possui um loop.  | Boolean  |
|[check_regular_graph](#verifica-a-regularidade-de-um-grafo) | ---   | Método que verifica a regularidade de um grafo.  | Boolean  |
|[incidence_list](#incidência-de-um-grafo) | ---   | Método que retorna uma lista de objetos que contem a incidencia dos vertices com as arestas.  | List<ValueBinding>  |
|[adjacency_matrix](#adjacência-de-um-grafo) | ---   | Método que retorna a representação em forma de matriz de adjacência do grafo.  | Dict  |
|[`__str__`](#representação-textual) | ---   | Método que retorna a representação textual do grafo.  | String  |


## Exemplos de uso:
Não faz muito sentido ter um grafo como esse, ele existe na biblioteca apenas para servir para reuso.

### Adicionar um vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_vertex("c")
~~~

### Deletar um vértice

~~~python3
grafo = Graph()
grafo.delete_vertex("a")
grafo.delete_vertex("b")
grafo.delete_vertex("c")
~~~

### Adicionar uma aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
~~~

### Deletar uma aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
grafo.delete_edge("a", "a")
~~~

### Visualizar aresta

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA")
print(grafo.show_edge("a", "b"))
~~~

### Verificar se um vértice é terminal de uma aresta

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

### Número de vértices

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.num_vertex())
~~~

### Número de arestas

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.num_edges())
~~~

### Verifica se um vértice existe

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.vertex_exists("a"))
~~~

### Verifica se uma aresta existe

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
print(grafo.edge_exists("a", "b"))
~~~

### Vizinhos de um vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.vertex_neighbors("a"))
~~~

### Grau do vértice

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.vertex_degree("a"))
~~~

### Verifica se os vértices são adjacentes

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.is_vertices_adjacents("a", "b"))
~~~

### Lista dos vértices do grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.get_all_vertex())
~~~

### Lista com todos os identificadores dos vértices

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.list_graph_vertices())
~~~

### Lista com os nomes das arestas

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
print(grafo.get_all_vertex())
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.list_graph_edges())
~~~

### Verifica se um grafo possui ciclos, loops também são detectados

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.has_cycle())
~~~

### Verifica se um grafo possui um loop

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.has_loop())
~~~

### Verifica a regularidade de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.check_regular_graph())
~~~

### Incidência de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.incidence_list())
~~~

### Adjacência de um grafo

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.adjacency_matrix())
~~~

### Representação textual

~~~python3
grafo = Graph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
print(grafo.__str__())
~~~
