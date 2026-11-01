def minimax(stones, is_max):

    if stones == 0:

        if is_max:
            return -1
        else:
            return 1

    if is_max:

        best = -1000

        for i in [1, 2]:

            if stones >= i:

                value = minimax(stones-i, False)

                best = max(best, value)

        return best

    else:

        best = 1000

        for i in [1, 2]:

            if stones >= i:

                value = minimax(stones-i, True)

                best = min(best, value)

        return best


stones = int(input("Enter number of stones: "))

while stones > 0:

    print("Stones remaining:", stones)

    move = int(input("Take 1 or 2 stones: "))

    if move not in [1, 2] or move > stones:
        print("Invalid move")
        continue

    stones -= move

    if stones == 0:
        print("You win!")
        break

    best_move = 1
    best_value = -1000

    for i in [1, 2]:

        if stones >= i:

            value = minimax(stones-i, False)

            if value > best_value:
                best_value = value
                best_move = i

    print("Computer takes", best_move, "stones")

    stones -= best_move

    if stones == 0:
        print("Computer wins!")