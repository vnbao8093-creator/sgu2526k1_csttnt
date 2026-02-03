import networkx as nx

def get_graph_data():
    # Danh sách kề dựa trên tài liệu
    return {
        'A': ['B', 'C', 'F'],
        'B': ['A', 'C', 'E', 'F'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['C', 'F'],
        'E': ['B', 'D', 'F'],
        'F': ['A', 'C', 'E']
    }

def giai_bai_1():
    adj = get_graph_data()
    G = nx.Graph()
    for node, neighbors in adj.items():
        for n in neighbors:
            G.add_edge(node, n)
    
    degrees = dict(G.degree())
    max_node = max(degrees, key=degrees.get)
    path = nx.shortest_path(G, source='A', target='D') # Tìm đường đi A -> D
    
    return G, degrees, max_node, path