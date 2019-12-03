# [Grafo Simples](https://github.com/Rickecr/PyGraph/blob/efc5d75006ac82773a4e7102c9d86d9e06ef31f2/py_graph_t/SimpleGraph.py#L11)
Esse é a representação do Grafo Simples. Herda características e métodos do [Graph](#graph.md), entretanto sobrescreve alguns métodos para que possa ser feito suas restrições específicas.

Restrições que esse tipo de grafo possui:

- Não contêm loops.
- Não contêm arestas paralelas.

Nessa implementação as arestas *não tem pesos*.

## Importar:

```python3
from py_graph_t import SimpleGraph
```

## Métodos:

Possui todos os métodos do [Graph](#graph.md), mas como tem restrições específicas foi necessário sobrescrever alguns métodos.

### Métodos sobrescritos:

| Método | Parâmetros | O que faz ? | Retorno |
----------------- | ---------- | --------- |--------- |
| [add_edge](#adicionar-uma-aresta)  | value_a, value_b, name(opcional) | Método que adiciona uma aresta ao grafo.  | SimpleEdge adicionado. |

## Exemplos de uso:

### Adicionar uma aresta

~~~python3
grafo = SimpleGraph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA")
grafo.add_edge("a", "a", name="Aresta AA") # Deve ser lançado um erro(loop)
~~~

~~~python3
grafo = SimpleGraph()
grafo.add_vertex("a")
grafo.add_vertex("b")
grafo.add_edge("a", "b", name="Aresta AB")
grafo.add_edge("b", "a", name="Aresta BA") # Deve lançar exceção(ciclo)
~~~