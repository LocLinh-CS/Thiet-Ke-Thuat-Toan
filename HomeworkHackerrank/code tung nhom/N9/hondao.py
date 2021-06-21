n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

def in_range(u, v):
    return (0 <= u and u < n) and (0 <= v and v < m)

island_num = 0
island_idx = [[0 for _ in range(m)] for _ in range(n)]
for start_u in range(n):
    for start_v in range(m):
        if grid[start_u][start_v] and not island_idx[start_u][start_v]:
            island_num += 1

            queue = [(start_u, start_v)]
            while len(queue):
                (u, v) = queue.pop(0)

                if island_idx[u][v]:
                    continue
                island_idx[u][v] = island_num

                for (delta_u, delta_v) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_u, next_v = u + delta_u, v + delta_v
                    if in_range(next_u, next_v) and grid[next_u][next_v]:
                        queue.append((next_u, next_v))

island_lim = [(n, m, 1, 1) for _ in range(island_num)]
for u in range(n):
    for v in range(m):
        if island_idx[u][v]:
            idx = island_idx[u][v] - 1
            (u_min, v_min, u_max, v_max) = island_lim[idx]
            u_min, v_min = min(u_min, u), min(v_min, v)
            u_max, v_max = max(u_max, u), max(v_max, v)
            island_lim[idx] = (u_min, v_min, u_max, v_max)

num_islands = island_num
for i in range(island_num):
    (u_min, v_min, u_max, v_max) = island_lim[i]
    if u_min == 0 or v_min == 0 or (u_max + 1) == n or (v_max + 1) == m:
        num_islands -= 1
print(num_islands)