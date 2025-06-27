import cpmpy as cp
from cpmpy.tools.explain import mus, mcs, mcs_opt
import networkx as nx
import re
import matplotlib.pyplot as plt

draw = lambda g, **kwargs: (nx.draw_circular(g, width=5, node_size=500, **kwargs), plt.show())
cmap = ["black", "yellow", "cyan", "lightgreen", "blue"]


def graph_coloring(graph, max_colors=None):
    nodes_num = graph.number_of_nodes()
    max_colors = max_colors if max_colors is not None else nodes_num

    m = cp.Model()
    # variables are the nodes, possible values are the colours
    nodes = cp.intvar(1, max_colors, shape=nodes_num, name="Node")
    # constrain edges to have differently colored nodes (i.e., not equal values)
    m.add([nodes[n1] != nodes[n2] for n1, n2 in graph.edges()])
    m.minimize(cp.max(nodes))  # minimize colours used!

    return m, nodes


def graph_highlight(graph, cons, **kwargs):
    edges = []
    for c in cons:
        n1, n2 = c.args
        if n1.name == "max": continue
        a = int(re.search("\[[0-9]*\]", str(n1)).group()[1:-1])
        b = int(re.search("\[[0-9]*\]", str(n2)).group()[1:-1])
        edges.append((a, b))

    colors = ["red" if (a, b) in edges else "black" for (a, b) in graph.edges()]
    return draw(graph, edge_color=colors, **kwargs)


G = nx.fast_gnp_random_graph(5, 0.8, seed=0)
m, nodes = graph_coloring(G, max_colors=3)

if m.solve():
    # print(f"Found optimal coloring with {m.objective_value()} colors")
    draw(G, node_color=[cmap[n.value()] for n in nodes])
else:
    print("No solution found.")


