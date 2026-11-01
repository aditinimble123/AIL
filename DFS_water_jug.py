def dfs(x, y, target):

    stack = [(0, 0)]
    visited = set()

    while stack:

        a, b = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        print(a, b)

        if a == target or b == target:
            print("Target Reached!")
            return

        # Possible operations
        stack.append((x, b))  # Fill jug 1
        stack.append((a, y))  # Fill jug 2
        stack.append((0, b))  # Empty jug 1
        stack.append((a, 0))  # Empty jug 2

        # Pour jug 1 into jug 2
        pour = min(a, y-b)
        stack.append((a-pour, b+pour))

        # Pour jug 2 into jug 1
        pour = min(b, x-a)
        stack.append((a+pour, b-pour))

    print("Solution not found")


x = 4
y = 3
target = 2

print("Water Jug Problem")
print("Jug 1 Capacity:", x)
print("Jug 2 Capacity:", y)
print("Target Amount:", target)

print("\nSteps:")
dfs(x, y, target)