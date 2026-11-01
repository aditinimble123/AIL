from collections import deque

# Robot path planning grid
# 0 = Free path
# 1 = Obstacle

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

def bfs(start, goal):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        if (x, y) not in visited:

            visited.add((x, y))

            moves = [(0,1), (1,0), (0,-1), (-1,0)]

            for dx, dy in moves:

                nx, ny = x + dx, y + dy

                if (0 <= nx < 4 and 0 <= ny < 4
                    and grid[nx][ny] == 0
                    and (nx, ny) not in visited):

                    queue.append(path + [(nx, ny)])

    return None


start = (0, 0)
goal = (3, 3)

print("Grid:")
for row in grid:
    print(row)

path = bfs(start, goal)

if path:
    print("\nRobot Path:", path)
    print("Steps:", len(path) - 1)
else:
    print("Path not found")