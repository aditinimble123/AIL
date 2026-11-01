import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i//3 - j//3) + abs(i%3 - j%3)
    return distance

def astar(start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if 0 <= new < 9:
                if abs(zero//3 - new//3) + abs(zero%3 - new%3) == 1:
                    temp = list(state)
                    temp[zero], temp[new] = temp[new], temp[zero]
                    temp = tuple(temp)

                    if temp not in visited:
                        h = heuristic(temp, goal)
                        heapq.heappush(pq, (cost + 1 + h, temp, path + [state]))

    return None

start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

result = astar(start, goal)

if result:
    for state in result:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found")