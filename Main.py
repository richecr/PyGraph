from py_graph_t.SimpleGraph import SimpleGraph
from py_graph_t.vertex.SimpleVertex import SimpleVertex

g = SimpleGraph()

g.add_vertex(1)
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

g.add_edge(1,"b",name="primeira_aresta")
g.add_edge("c", "d")
g.add_edge(1, "d", name="terceira_aresta")

print(g.__str__())
print(g.get_all_vertex())

g.delete_edge(1, "d")
print(g.__str__())

g.delete_vertex(1)
print(g.__str__())
print(g.get_all_vertex())

g.add_vertex("b")
print(g.get_all_vertex())
'''
print(g.list_graph_vertices())
#print(g.vertices)

#g.delete_vertex(1)



print(g.edges)
print(g.vertex_neighbors(1))
print(g.show_edge(1, "d"))

g.delete_edge(1, "b")
print(g)


print(g.__str__())
print(g.num_vertex())
print(g.num_edges())
print(g.vertex_exists(SimpleVertex("c")))
print(g.vertex_exists(SimpleVertex(2)))

# print(g.vertex_degree(2))
print(g.vertex_neighbors("c"))

print(g.vertex_neighbors(1))
print(g.vertices_adjacency(1, "b"))
print(g.list_graph_vertices())
print(g.list_graph_edges())
'''