from py_graph_t.Graph import Graph

g = Graph()

g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")

g.add_edge("a", "b", name="s")
g.add_edge("b", "c", name="t")
g.add_edge("a", "a", name="d")

i = g.incidence_list()
print(i)
print(g.__str__())
