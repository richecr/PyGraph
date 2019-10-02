from py_graph_t.SimpleGraph import SimpleGraph
from py_graph_t.vertex.SimpleVertex import SimpleVertex

g = SimpleGraph()

g.add_vertex(1)
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

g.add_edge(name="primeira_aresta", vertex_a=1, vertex_b="b")
g.add_edge(vertex_a="c", vertex_b="d")
g.add_edge(name="terceira_aresta", vertex_a=1, vertex_b="d")

print(g.__str__())
print(g.num_vertex())
print(g.num_edges())
print(g.vertex_exists(SimpleVertex("c")))
print(g.vertex_exists(SimpleVertex(2)))

g.delete_vertex(SimpleVertex(1))
print(g.__str__())
print(g.num_vertex())
print(g.num_edges())

g.delete_vertex(SimpleVertex(5))
print(g.__str__())
print(g.num_vertex())
print(g.num_edges())
'''
print(g.vertex_neighbors(1))
print(g.vertices_adjacency(1, "b"))
print(g.list_graph_vertices())
print(g.list_graph_edges())
'''