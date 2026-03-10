def read_file(f="TOMAU.INP"):
    with open(f, "r") as file:
        data = file.read().strip().split()
    
    n = int(data[0])
    edges = []
    
    for i in range(1, len(data), 2):
        u = int(data[i])
        v = int(data[i+1])
        edges.append((u, v))
        
    return n, edges


def build_graph(n, edges):
    adj = [[] for _ in range(n+1)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    return adj


def is_safe(v, c, color, adj):
    for u in adj[v]:
        if color[u] == c:
            return False
    return True


def backtrack(v, n, k, color, adj):
    if v > n:
        return True
    
    for c in range(1, k+1):
        if is_safe(v, c, color, adj):
            color[v] = c
            
            if backtrack(v+1, n, k, color, adj):
                return True
            
            color[v] = 0
    
    return False


def graph_coloring(n, adj):
    for k in range(1, n+1):
        color = [0]*(n+1)
        
        if backtrack(1, n, k, color, adj):
            return k, color
    
    return None


def print_result(k, color, n):
    print(k)
    
    groups = [[] for _ in range(k+1)]
    
    for i in range(1, n+1):
        groups[color[i]].append(i)
    
    for i in range(1, k+1):
        print(*groups[i])


def main():
    n, edges = read_file()
    adj = build_graph(n, edges)
    
    k, color = graph_coloring(n, adj)
    
    print_result(k, color, n)


if __name__ == "__main__":
    main()