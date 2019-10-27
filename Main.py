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
'''
graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")

graph.add_edge("a", "b", name="s")
graph.add_edge("a", "a", name="t")
graph.add_edge("b", "c", name="u")
graph.add_edge("c", "d", name="v")
graph.add_edge("c", "d", name="w")
graph.add_edge("d", "b", name="x")
graph.add_edge("a", "d", name="y")
graph.add_edge("e", "d", name="z")
adjacency_matrix =  graph.adjacency_matrix()
for line in adjacency_matrix:
    print(line, adjacency_matrix[line])
'''
