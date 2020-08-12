import keyboard
import pyfiglet
import random

number = random.randint(0,9)
no_of_guesses = 0

banner = pyfiglet.figlet_format("Guess The Number")
print(banner)
print("Game by 2kwattz \nTries Left:10")

while (no_of_guesses<10):
    no_of_guesses = no_of_guesses + 1
    guess = int(input("Enter the number\n"))
    if no_of_guesses>9:
        print("Game Over\n")
        break

    if guess>number:
        print(f"Enter a smaller number , {no_of_guesses} tries done")

    elif guess<number:
        print(f"enter a bigger number number , {no_of_guesses} tries done")

    elif guess == number:
        print(f"Congratulations! You guessed the number correct! \n The number is {number} \n")
        break
    else:
        print("Please enter a valid number\n")
        break

        print("Program end . Press ESC to continue\n")
        keyboard.wait("esc")
