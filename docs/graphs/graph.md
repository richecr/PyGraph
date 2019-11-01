# [Grafo Base](https://github.com/Rickecr/PyGraph/blob/deb3fa4cb011f42255dd48ee4c54660205928af2/py_graph_t/Graph.py#L12)
Esse é o grafo que todos os outros grafos vão herdar suas características/métodos.

Esse grafo não possui nenhum tipo de restrição. Pois todos os outros grafos irão sobrescrever os métodos necessários para aplicar suas restrições.

## Métodos:

| Método | Parâmetros | O que faz ? | Retorno |
----------------- | ---------- | --------- |--------- |
| `addVertex`       |   value    |  Método que adiciona um vértice ao grafo.       | SimpleVertex adicionado |
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