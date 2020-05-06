import networkx as nx
from functions.weighted_graph_drawings import show_weighted_graph
from functions.weighted_graph_drawings import draw_subtree
from functions.prims_functions import min_prims_edge, cost



        
def prims_algorithm(G, starting_node, draw = False, detail = False):
    
     """Returns minimum spanning subtree of graph 'G'. Displays every iteration as 
     algorithm constructs subtree. After last iteration algorithm displays vertices, edges
     and total cost of subtree.
    
    A minimum spanning tree is a subtree of graph using all vertices while staying
    connected and having minimum possible weight while meeting first two conditions.
    
    Total cost of a tree is the sum of all edges. Also referred to as total weight.
    
    A subtree is a tree graph inside of another graph.
    
    Parameters
    ----------
    G = A networkx graph.
    starting_node = A node on 'G'.
    draw = A bool value.
    detail = A bool value.
    
    Returns
    -------
    T a subgraph of G. Including nodes, edges and weights.
    
    Examples
    --------
    >>> G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    >>> starting_node = 2
    
    >>> draw = True
    
    >>> detail = True
    
    ------------------Tree T Details---------------
-----------------------------------------------
V(T) = [3, 5, 6, 2, 1, 0, 4, 7]
E(T) = [(3, 5), (3, 2), (5, 6), (6, 7), (2, 1), (2, 0), (0, 4)]
Total Cost = 12.0
----------------------------------------------
    """
    
     T = nx.Graph()
     T.add_node(starting_node)
     if draw == True:
        draw_subtree(G,T)
        
     while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edge(G,T)
        T.add_edge(e[0],e[1], weight = cost(G,e))
        if draw == True:
            draw_subtree(G,T)
    
     if detail == True:
        total_cost = sum(cost(G, e) for e in T.edges())
        print('------------------Tree T Details---------------')
        print('-----------------------------------------------')
        print(f'V(T) = {list(T.nodes())}')
        print(f'E(T) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print(f'----------------------------------------------')
     return T

