import textwrap
number = 78
no_of_guesses = 0

textwrap.shorten("Guess Me", width=12)
'Hello world!'
print("Game by Roshan Bhatia \n Tries Left:10")

while (no_of_guesses<10):
    no_of_guesses = no_of_guesses + 1
    guess = int(input("Enter the number\n"))
    if no_of_guesses>9:
        print("Game Over\n")
        break

    if guess>number:
        print(f"Enter a smaller number , {no_of_guesses} tries done\n")

    elif guess<number:
        print(f"enter a bigger number number , {no_of_guesses} tries done\n")

    elif guess == number:
        print(f"Congratulations! You guessed the number correct! \n The number is {number} \n")
        break
    else:
        print("Please enter a valid number\n")
        break
