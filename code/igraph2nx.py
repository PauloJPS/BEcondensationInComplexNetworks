import igraph as ig
import networkx as nx


def ig2nx(g):
    gnx = nx.Graph()
    node_att = [(node.index, node.attributes()) for node in g.vs]
    gnx.add_nodes_from(node_att)
    edge_att = [(edge.source, edge.target, edge.attributes()) for edge in g.es]
    gnx.add_edges_from(edge_att)

    return gnx

