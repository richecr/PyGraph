from graph.SimpleGraph import SimpleGraph

g = SimpleGraph()

g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")

g.add_edge(node_a="a", node_b="b")
g.add_edge(node_a="c", node_b="d")
g.add_edge(node_a="a", node_b="d")
g.add_edge(node_a="c", node_b="b")

print(g.__str__())