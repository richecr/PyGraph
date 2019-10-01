from graph.SimpleGraph import SimpleGraph

g = SimpleGraph()

g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

g.add_edge(vertex_a="a", vertex_b="b")
g.add_edge(vertex_a="c", vertex_b="d")
g.add_edge(vertex_a="a", vertex_b="d")

print(g.__str__())
print(g.num_vertex())
print(g.num_edges())