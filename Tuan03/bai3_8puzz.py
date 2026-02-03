from collections import deque

def giai_bai_3():
    # Trạng thái ban đầu và đích (0 là ô trống)
    start = (4, 8, 1, 6, 3, 0, 2, 7, 5) 
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    def get_moves(state):
        res = []; i = state.index(0); r, c = divmod(i, 3)
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: # Luật di chuyển ô trống
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                ni = nr * 3 + nc; s = list(state)
                s[i], s[ni] = s[ni], s[i]; res.append(tuple(s))
        return res

    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        curr, path = queue.popleft()
        if curr == goal: return path
        for nxt in get_moves(curr):
            if nxt not in visited:
                visited.add(nxt); queue.append((nxt, path + [nxt]))
    return None