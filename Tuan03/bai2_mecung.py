from collections import deque

def giai_bai_2():
    # 0: đường đi, 1: tường. Tọa độ (0,0) là con kiến, (5,5) là ô A
    maze = [
        [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]
    ]
    start, goal = (0, 0), (5, 5)
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (r, c), path = queue.popleft() # Sử dụng BFS
        if (r, c) == goal: return path
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: # Di chuyển 4 hướng
            nr, nc = r + dr, c + dc
            if 0 <= nr < 6 and 0 <= nc < 6 and maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None