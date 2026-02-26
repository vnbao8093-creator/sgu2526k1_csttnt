import pprint
G = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['A', 'B', 'D', 'F'],
    'D': ['C', 'F'],
    'E': ['B', 'D', 'F'],
    'F': ['A', 'C', 'E']
}

def tinh_bac(G):
    bac = {}
    for dinh in G:
        bac[dinh] = len(G[dinh])
    return bac
bac_cac_dinh = tinh_bac(G)
print("Bậc của từng đỉnh:")
for dinh, b in bac_cac_dinh.items():
    print(f"{dinh}: {b}")
bac_max = max(bac_cac_dinh.values())
print("Bậc cao nhất của đồ thị:", bac_max)

def BFS(G, start, goal):
    result = None
    if G.get(start) is None or G.get(goal) is None:
        result = None
    else:
        path = {}
        s_open   = []
        s_closed = []
        s_open.append(start)    
        path[start] = None
        while len(s_open)>0:
            u = s_open.pop(0)    
            s_closed.append(u)
            if u == goal:
                break
            for v in G[u]:
                if v not in s_open and v not in s_closed:
                    s_open.append(v)
                    path[v] = u
        pass
    return path
path = BFS(G, "A", "D")
pprint.pprint(path)
def find_path(path, start, goal):
    result = []
    if start == goal:
        return [start]
    
    if goal not in path:
        return []
    
    cur = goal
    while cur != start:
        result.append(cur)
        cur = path.get(cur)
        
        if cur is None:
            return []
    
    result.append(start)
    result.reverse()
    
    return result
duong_di = find_path(path, "A", "D")  
print(duong_di)
import networkx as nx
import matplotlib.pyplot as plt
def ve_do_thi_co_duong_di(G, path):
    graph = nx.Graph()
    for u in G:
        for v in G[u]:
            graph.add_edge(u, v)
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=1500,
        alpha=0.6
    )
    if path and len(path) > 1:
        edges_path = []
        for i in range(len(path)-1):
            edges_path.append((path[i], path[i+1]))
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=edges_path,
            width=3
        )
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=path,
            node_size=1700
        )
    plt.title("Đồ thị và đường đi BFS")
    plt.savefig("duongdi.png")
    plt.close()
ve_do_thi_co_duong_di(G, duong_di)
