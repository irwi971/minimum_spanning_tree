

def cost(graph,e):
    
    """Return the cost of an edge on a graph.
    
    The cost of an edge is also called its weight.
    
    Parameters
    ----------
    G = A networkx graph.
    e = An edge on graph.
    
    Returns
    -------
    The weight of an edge 'e' on a graph 'graph'.
    
    Examples
    --------
    >>> graph = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    >>> e = (3,5)
    1
    """
    
    return graph.edges[e]['weight']


def is_spanning(graph, subgraph):
    
     """Return True or False.
    
    When a subgraph is spanning it uses all vertices(nodes) of the original graph.
    
    Parameters
    ----------
    graph = A networkx graph.
    subgraph = A networkx subgraph of 'graph'.
    
    Returns
    -------
    True if the subgraph is spanning.
    False if the subgraph is not spanning.
    
    Examples
    --------
    >>> graph = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    >>> T = nx.graph()
    """
    
     return graph.nodes()== subgraph.nodes()


def incident_edges(graph,tree):
    
     """Returns the valid incident edges.
     
     An incident edge is an edge that is adjacent to the node that is
     being evaluated. An edge is valid when both endpoints are not not already in
     the set containting tree nodes.
    
    Parameters
    ----------
    graph = A networkx graph.
    tree = A networkx subgraph of 'graph'.
    
    Returns
    -------
    A set of valid incident edges.
    
    Examples
    --------
    In example tree already contains node 2.
    
    >>> graph = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    >>> tree = nx.graph()
    [(2,1),(2,0),(2,3),(2,5)]
    """
    
     possible_edges =[]
     for e in graph.edges():
        for v in tree.nodes():
            if v in e:
                possible_edges.append(e)
              
     valid_edges = []
     for e in possible_edges:
        if e[0] not in tree.nodes() or e[1] not in tree.nodes():
            valid_edges.append(e)
    
     return valid_edges


def min_prims_edge(G, T):
    
     """Return the minimum cost incident edge from a set created by the incident 
     edge function. Uses the cost function to determine the minimum cost edge.
    
    The minimum cost edge is the edge with the lowest weight.
    
    Parameters
    ----------
    G = A networkx graph.
    T = A networkx subgraph of 'graph'.
    
    Returns
    -------
    The weight of an edge 'e' on a graph 'graph'.
    
    Examples
    --------
    In example 'Incident_edges' has returned valid edges from node 2. 
    
    >>> G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    >>> T = nx.graph()
    [(1,2)]
    """
    
     possible_e = incident_edges(G,T)
     min_e = possible_e[0]              
     for e in possible_e:
        if cost(G,e) < cost(G,min_e):
            min_e = e
     return min_e



