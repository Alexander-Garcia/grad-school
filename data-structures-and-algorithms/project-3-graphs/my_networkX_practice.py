from random import randint

import matplotlib.pyplot as plt
import networkx as nx

# adj list representation of a graph
# key: Node, value: list of adj nodes
adj_list: dict[str, list[str]] = {
    "A": ["E", "F"],
    "B": ["F", "G"],
    "C": ["G", "H"],
    "D": ["E", "N"],
    "E": ["A", "D", "I"],
    "F": ["A", "B", "E", "G", "J"],
    "G": ["B", "C", "F", "H", "K"],
    "H": ["C", "G", "L", "M"],
    "I": ["E", "J", "N"],
    "J": ["F", "I", "K", "O"],
    "K": ["G", "J", "L", "P"],
    "L": ["H", "K", "Q"],
    "M": ["H", "Q"],
    "N": ["D", "I", "O", "R"],
    "O": ["J", "N", "P", "R"],
    "P": ["K", "O", "Q", "S"],
    "Q": ["L", "M", "P", "T"],
    "R": ["N", "O"],
    "S": ["O", "P"],
    "T": ["P", "Q"],
}


def build_graph():
    """Builds a networkx graph from adj_list.

    Weights are added with randint to each edge for all edges in G.edges

    Returns
    --------
    G: NetworkX graph
    """
    G = nx.Graph(adj_list)
    weights = {edges: {"weight": randint(1, 15)} for edges in G.edges}
    nx.set_edge_attributes(G, weights)
    return G


def bellman(G, source_node: str) -> list[tuple[str, str]]:
    """Runs the bellman single source algorithm on graph G.

    The single source bellman returns distance and path. Use the path
    which shows shortest distance from source_node to all other nodes to build
    the edges for visualizing the algorithm

    Parameters
    ----------
    G: NetworkX Graph
    source_node: str
        Node at which to start the Bellman-ford algorithm.

    Returns
    --------
    bellman_edges: list[tuple[str,str]]
        List of tuples that represent the edges (u,v) bellman travels
    """
    _, path = nx.single_source_bellman_ford(G, source_node)
    # k:string - node, v:list[str] - path to that node from source
    # use this to build the edges bellman travels
    bellman_edges: list[tuple[str, str]] = []
    for k, v in path.items():
        if k == source_node:
            continue
        edges = [(v[e], v[e + 1]) for e in range(len(v) - 1)]
        bellman_edges.extend(edges)

    return bellman_edges


def show_multi_graph(G, T) -> None:
    """Shows the source graph G with an overlay of another algorithm such as MST.

    Visualizes the source G and then overlays the resulting edges of other algorithms
    such as kruskal, prim, bellman, etc...

    Parameters
    ----------
    G: NetworkX Graph
    T: NetworkX Graph
        The graph returned from other NetworkX algorithms.

    Returns
    --------
    None

    See Also
    --------
    For references of visualizing see
    https://networkx.org/documentation/stable/auto_examples/index.html
    """
    pos = nx.spring_layout(G, weight=None, seed=7)
    nx.draw(G, pos, with_labels=True, node_color="lightyellow")
    # get the weights of each edge
    edge_weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    nx.draw_networkx_edges(T, pos, edge_color="blue", width=2)
    plt.show()


def show_single_graph(G) -> None:
    """Visualizes source graph G.

    Parameters
    ----------
    G: NetworkX Graph

    Returns
    --------
    None

    See Also
    --------
    For references of visualizing see
    https://networkx.org/documentation/stable/auto_examples/index.html
    """
    pos = nx.spring_layout(G, weight=None, seed=7)
    nx.draw(G, pos, with_labels=True, node_color="lightyellow")
    # get the weights of each edge
    edge_weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.show()


def show_tree(G) -> None:
    """Visualizes a graph G without weights added to edge labels

    Parameters
    ----------
    G: NetworkX Graph

    Returns
    --------
    None

    See Also
    --------
    For references of visualizing see
    https://networkx.org/documentation/stable/auto_examples/index.html
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightyellow")
    plt.show()


if __name__ == "__main__":
    # build the main NetworkX graph
    G = build_graph()
    # copy the graph into a directed graph
    DG = G.to_directed()
    # run MST algorithms of Prim and Kruskal
    P = nx.minimum_spanning_tree(G, weight="weight", algorithm="prim")
    K = nx.minimum_spanning_tree(G, weight="weight", algorithm="kruskal")
    # run bellman-Ford algorithm on the directed graph with source node A
    bellman_edges = bellman(DG, "A")
    # build graph from bellman edges to overlay on directed graph
    BG = nx.Graph(bellman_edges)
    # visualize the two types of graphs before running algorithms on them
    show_single_graph(G)
    show_single_graph(DG)
    # visualize directed graph with bellman algorithm
    show_multi_graph(DG, BG)
    # visualize Prim and Kruskals algorithm
    show_multi_graph(G, P)
    show_multi_graph(G, K)
    BFS_Tree = nx.bfs_tree(G, "A")
    show_tree(BFS_Tree)
    DFS_Tree = nx.dfs_tree(G, "A")
    show_tree(DFS_Tree)
