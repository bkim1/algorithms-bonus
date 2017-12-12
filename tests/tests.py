import unittest
import random
import networkx as nx
import pythonds as ds
import src.boruvka as Boruvka
import src.prim as Prim

def construct_nx_graph(graph):
    '''Constructs the directed graph using the NetworkX library and 
    adds all nodes, edges, and weights from input dict

    Argument:
        g -- input dictionary representing graph
    Returns:
        NetworkX's directed graph with same nodes, edges, and weights
    '''
    g = nx.Graph()
    for node in graph:
        g.add_node(node)

    for node in graph:
        for edge, weight in graph[node]:
            g.add_edge(node, edge, weight=weight)

    return g

def construct_ds_graph(graph):
    g = ds.Graph()
    for node in graph:
        for edge, weight in graph[node]:
            g.addEdge(node, edge, cost=weight)
    
    return g

def rand_graphs():
    '''Constructs set directed graph with random weights with a graph 
    that has 7 nodes with set edges but randomized weights

    Returns:
        dict representing graph and a NetworkX version
    '''
    weights = [[rand_weight() for _ in range(12)] for i in range(12)]

    g = {0: [(1, weights[0][1]), (5, weights[0][5]), (6, weights[0][6])],
         1: [(0, weights[0][1]), (2, weights[1][2]), (6, weights[1][6])],
         2: [(1, weights[1][2]), (3, weights[2][3]), (6, weights[2][6])],
         3: [(2, weights[2][3]), (4, weights[3][4]), (6, weights[3][6])],
         4: [(3, weights[3][4]), (5, weights[4][5]), (6, weights[4][6])],
         5: [(0, weights[0][5]), (4, weights[4][5]), (6, weights[5][6])],
         6: [(0, weights[0][6]), (1, weights[1][6]), (2, weights[2][6]),
             (3, weights[3][6]), (4, weights[4][6]), (5, weights[5][6])]
    }

    return (g, construct_nx_graph(g), construct_ds_graph(g))

def rand_weight(start=1, end=100):
    '''Returns random weight for graph'''
    return random.randint(start, end)

class TestAlg(unittest.TestCase):
    def test_correctness(self):
        g, nx_g, ds_g = rand_graphs()

        # p_weight = Prim.prim(ds_g, ds_g.getVertex(0))
        b_weight = Boruvka.boruvka(g)
        print(g)
        print('\n')
        print(nx_g.edge)
        
        nx_weight = 0
        nx_edges = nx.minimum_spanning_edges(nx_g)
        for u, v, w in nx_edges:
            print(w)
            nx_weight += w['weight']

        # self.assertEqual(p_weight, nx_weight)
        self.assertEqual(b_weight, nx_weight)



if __name__ == '__main__':
    unittest.main()