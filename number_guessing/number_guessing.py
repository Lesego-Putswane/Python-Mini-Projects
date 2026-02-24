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

def play_again():
    print("Would you like to play again?")
    replay = input("Enter choice(y/n): ")
    
    if replay == "n".lower():
        print("See you again next time")
        exit()
    elif replay == "y".lower():
        print("Great Choice! Enjoy the game \n")
        number_guessing_game()

def number_guessing_game():
    lucky_number = random.randint(1, 100)
    tries = 5

    for i in range(tries):
        user_number = int(input("Enter a number between 1 - 100: "))
        tries -= 1

        if user_number == lucky_number:
            print(f"Great Job! {user_number} is the lucky number")
            break
        elif user_number > lucky_number:
            print(f"{user_number} is too HIGH. You have {tries} tries remaining.")
        elif user_number < lucky_number:
            print(f"{user_number} is too low. You have {tries} tries remaining.")

            if tries == 0:
                print("GAME OVER \n")
                play_again()

def greetings():
    username = input("Enter your userusername: \n").lower()
    print(f"Welcome to the number guessing game, {username}! \nWould you like to play?")
    user_choice = input("Enter your choice (y/n): ")

    if user_choice == "y".lower():
        print("Great choice! Have fun. \n")
        number_guessing_game()
    elif user_choice == "n".lower():
        print("Sad to see you go. Come back again. BYE!")
        exit()

greetings()