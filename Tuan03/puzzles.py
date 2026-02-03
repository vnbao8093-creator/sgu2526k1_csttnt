import heapq

# Trạng thái đích
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Tính Manhattan distance
def manhattan(state):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            dist += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return dist

# Các bước di chuyển hợp lệ
def neighbors(state):
    idx = state.index(0)
    x, y = idx // 3, idx % 3
    moves = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # U D L R
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            nidx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
            moves.append(tuple(new_state))
    return moves

# Thuật toán A*
def solve_8_puzzle(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for nxt in neighbors(state):
            if nxt not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(nxt), g + 1, nxt, path + [state])
                )
    return None

# ======= CHẠY THỬ =======
start_state = (4, 8, 1,
               6, 3, 0,
               2, 7, 5)

solution = solve_8_puzzle(start_state)

if solution:
    print("Số bước:", len(solution) - 1)
    for s in solution:
        print(s[0:3])
        print(s[3:6])
        print(s[6:9])
        print()
else:
    print("Không có lời giải")
