def minimax(depth, node, alpha, beta, maximizing):
    if depth == 3:
        return node

    if maximizing:
        best = -1000

        for child in [3, 5]:
            value = minimax(depth + 1, child, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for child in [2, 9]:
            value = minimax(depth + 1, child, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

result = minimax(0, 0, -1000, 1000, True)

print("Best value:", result)