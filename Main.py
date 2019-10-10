from py_graph_t.SimpleGraph import SimpleGraph

g = SimpleGraph()

g.add_vertex(1)

g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

g.add_edge(1, "b", name="primeira_aresta")
g.add_edge("c", "d")
g.add_edge(1, "d", name="terceira_aresta")

a = g.delete_edge(1, 'c')
print(a)
print("-------")
print(g.__str__())
