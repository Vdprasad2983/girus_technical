from collections import deque

def shortest_path_with_teleport(grid):
    R, C = len(grid), len(grid[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    empty = [(i,j) for i in range(R) for j in range(C) if grid[i][j]==0]
    visited = [[False]*C for _ in range(R)]
    q = deque([(0,0,False,0)])
    visited[0][0] = True

    while q:
        r,c,used,dist = q.popleft()
        if (r,c) == (R-1,C-1): return dist

        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==0:
                visited[nr][nc] = True
                q.append((nr,nc,used,dist+1))

        if not used:
            for er,ec in empty:
                if not visited[er][ec]:
                    visited[er][ec] = True
                    q.append((er,ec,True,dist+1))

    return -1

# Test Case
grid = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0]
]
print("Shortest Path:", shortest_path_with_teleport(grid))
