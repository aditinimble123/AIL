low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:

    guess = (low + high) // 2

    print("My guess is:", guess)

    answer = input("Enter H for higher, L for lower, C for correct: ").lower()

    if answer == 'c':

        print("Correct! I guessed your number.")
        break

    elif answer == 'h':

        low = guess + 1

    elif answer == 'l':

        high = guess - 1

    else:

        print("Invalid input")

else:
    print("Your answers are inconsistent.")