from py_graph_t.Graph import Graph

g = Graph()

g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")

g.add_edge("a", "b", name="primeira_aresta")
g.add_edge("b", "c")
try:
    g.add_edge("c", "a", name="terceira_aresta")
except Exception as identifier:
    pass


print(g.__str__())
