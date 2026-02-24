'''
Task: Create a number guessing game:
The user should have a limited number of attempts (e.g., 5 tries).
Keep track of how many guesses they took.
Give them a message if they fail to guess in the given attempts.
Ask them if they want to play again after the game ends.
This adds layers of logic, user flow, and program control,
very much like a “real mini app.”
'''
import random

def greetings():
    username = input("Enter your username: ").strip().lower()
    print(f"\nWelcome to the number guessing game, {username}.")
    print("Lets's begin.\n")

def number_guessing_game():
    lucky_number = random.randint(1, 100)
    game_tries = 5

    while game_tries > 0:
        try:
            user_number = int(input("Enter your lucky number(1 - 100): "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        game_tries -= 1

        if user_number == lucky_number:
            print(f"Great Job! {user_number} is the lucky number")
            return True
        elif user_number > lucky_number:
            print(f"{user_number} is too HIGH. You have {game_tries} tries remaining.")
        else:
            print(f"{user_number} is too low. You have {game_tries} tries remaining.")
        
    print("GAME OVER\n")
    return False
        
def play_again():
    while True:
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        
        if replay == "y".lower():
            print("Great choice. Starting a new game. . .\n")
            return True
        elif replay == "n".lower():
            print("See you again next time!")
            return False
        else:
            print("Please enter y or 'n'.\n")

def main():
    greetings()

    while True:
        number_guessing_game()

        if not play_again():
            break
    
main()

