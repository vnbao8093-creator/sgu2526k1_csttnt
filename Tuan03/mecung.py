import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
maze = [
    ['S', 0, 1, 0, 0, 0, 0],
    [ 0 , 0, 1, 0, 0, 0, 0],
    [ 0 , 0, 0, 0, 0, 1, 1],
    [ 0 , 0, 0, 0, 0, 0, 0],
    [ 0 , 0, 0, 0, 0, 0, 0],
    [ 0 , 1, 0, 0, 0, 0, 0],
    [ 0 , 1, 0, 0, 0, 0, 'A']
]
rows, cols = len(maze), len(maze[0])

#tim vi tri
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'A':
            goal = (i, j)
#BFS tim duong di
queue = deque([start])
visited = set([start])
parent = {}
directions = [(-1,0), (1,0), (0,-1), (0,1)]
while queue:
    x, y = queue.popleft()
    if (x, y) == goal:
        break
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] != 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
#truy vet duong di
path = []
cur = goal
while cur != start:
    path.append(cur)
    cur = parent.get(cur)
    if cur is None:
        print("Khong co duong di")
        path = []
        break
if path:
    path.append(start)
    path.reverse()
print("Đuonng di:", path)
#ve me cung
plt.figure(figsize=(6, 6))
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 1:
            plt.scatter(j, -i, c="black", s=600)
        else:
            plt.scatter(j, -i, c="lightgray", s=600)
if path:
    xs = [y for x, y in path]
    ys = [-x for x, y in path]
    plt.plot(xs, ys, c="orange", linewidth=4)
plt.scatter(start[1], -start[0], c="green", s=700)
plt.text(start[1], -start[0], "S", color="white",
         ha="center", va="center", fontweight="bold")
plt.scatter(goal[1], -goal[0], c="red", s=700)
plt.text(goal[1], -goal[0], "A", color="white",
         ha="center", va="center", fontweight="bold")
plt.title("Me cung - BFS tim duong di")
plt.savefig("duongditrongmecung.png")
plt.show()
