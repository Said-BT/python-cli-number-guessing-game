import random

def welcome():
    print()
    print("Welcome to the Number Guessing Game!")
    print("I will think of a number between 1 and 100.")
    print()

def rules():
    print("You will have 10, 5 or 3 chances to guess the correct number, based on the difficulty you will choose")
    print("After each guess, I will let you know if the number you selected is greater or less than the correct number")
    print()
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print()

def get_difficulty_level():
    while True:
        try:
            selected_level = int(input("Enter your difficulty level choice: "))
            if selected_level not in [1, 2, 3]:
                print("Please enter a valid number: 1, 2 or 3")
                continue

            return selected_level

        except ValueError:
            print("Please enter a valid number: 1, 2 or 3")

def get_number_of_max_attempts(selected_level):
    levels = {
        1: ("Easy", 10),
        2: ("Medium", 5),
        3: ("hard", 3)
    }
    print()
    name, chances = levels[selected_level]

    print(f"Great! You have selected the {name} difficulty level.")
    print(f"You have {chances} chances to guess the number")
    print()

    return chances

def play(correct_number, max_attempts):
    attempts = 0

    while True:
        try:
            guessed_number = int(input("Enter your guess: "))

            if guessed_number > 100 or guessed_number < 1:
                print("Please enter a valid number between 1 and 100")
                continue

        except ValueError:
            print("Please enter a valid number between 1 and 100")

        attempts += 1

        if guessed_number == correct_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return True

        elif attempts == max_attempts:
            print("Unfortunately, you ran out of chances. Round Over!")
            print(f"The correct number was {correct_number}")
            return False

        elif guessed_number > correct_number:
            print(f"Incorrect! The number is less than {guessed_number}.")

        else:
            print(f"Incorrect! The number is greater than {guessed_number}.")

def want_to_play_again():
    while True:
        play_again = input("Would you like to play another round(y, n)? :").strip().lower()
        if play_again == "n" or play_again == "no":
            return False
        elif play_again == "y" or play_again == "yes":
            return True
        else:
            print("Please enter 'y' for yes, or 'n' for no")

if __name__ == "__main__":
    rounds = 0
    wins = 0
    losses = 0

    welcome()
    rules()

    print("Let's start the game!")

    while True:

        selected_level = get_difficulty_level()
        chances = get_number_of_max_attempts(selected_level)

        # Using the random module to select a random number between 1 and 100:
        correct_number = random.randint(1, 100)

        # play return True if user won, False if user loses:
        did_user_win = play(correct_number, chances)

        rounds += 1

        if did_user_win:
            wins += 1
        else:
            losses += 1

        print()
        print(f"You have played {rounds} rounds, won {wins} and lost {losses}")

        if not want_to_play_again():
            print()
            print("Thank you for playing!")
            print("Have a nice day.")
            break

        else:
            print()
            print("Let's play another round")
