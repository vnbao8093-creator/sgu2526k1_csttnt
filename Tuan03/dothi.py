G = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['A', 'B', 'D', 'F'],
    'D': ['C', 'E', 'F'],
    'E': ['B', 'D', 'F'],
    'F': ['A', 'B', 'C', 'D', 'E']
}
import pprint

def BFS(G, start, goal):
    """
    return: 
    + mảng path: path[a] = b (muốn tới a thì đi qua b)
    + None: nếu start hoặc goal không hợp lệ
    """
    if G.get(start) is None or G.get(goal) is None:
        return None
    else:
        path = {}     # path[a] = b : muốn tới a thì đi qua b
        s_open   = []
        s_closed = []
        
        # đưa start vào open
        s_open.append(start)    
        path[start] = None

        while len(s_open) > 0:
            current = s_open.pop(0)   # lấy đỉnh đầu hàng đợi
            s_closed.append(current)

            # nếu đã tới goal thì dừng
            if current == goal:
                break

            # duyệt các đỉnh kề
            for neighbor in G[current]:
                if neighbor not in s_open and neighbor not in s_closed:
                    s_open.append(neighbor)
                    path[neighbor] = current
        
        return path
def trace_path(path, start, goal):
    if goal not in path:
        return []   # không có đường đi
    
    result = []
    current = goal
    while current is not None:
        result.append(current)
        current = path[current]
    
    result.reverse()
    return result
start = 'A'
goal = 'D'

path = BFS(G, start, goal)
print("Bảng path:")
pprint.pprint(path)

duong_di = trace_path(path, start, goal)
print("Đường đi từ", start, "đến", goal, "là:", duong_di)
import networkx as nx
import matplotlib.pyplot as plt

# Khai báo đồ thị
G = nx.Graph()

edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'F'),
    ('B', 'C'), ('B', 'E'), ('B', 'F'),
    ('C', 'D'), ('C', 'F'),
    ('D', 'E'), ('D', 'F'),
    ('E', 'F')
]

G.add_edges_from(edges)

# Đường đi BFS tìm được
path = ['A', 'C', 'D']
path_edges = list(zip(path, path[1:]))

# Vị trí các đỉnh
pos = nx.spring_layout(G, seed=42)

# Vẽ toàn bộ đồ thị
nx.draw(
    G, pos,
    with_labels=True,
    node_size=2000,
    node_color='lightblue',
    font_size=12,
    edge_color='gray',
    width=2
)

# Vẽ nổi bật đường đi BFS
nx.draw_networkx_edges(
    G, pos,
    edgelist=path_edges,
    edge_color='red',
    width=4
)

plt.title("Đồ thị và đường đi BFS từ A đến D", fontsize=14)
plt.savefig('graph_bfs_path.png')
print("Hình ảnh đã được lưu thành file 'graph_bfs_path.png'")
