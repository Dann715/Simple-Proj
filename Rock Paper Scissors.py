import random

def get_users_choice():
    while True:
        users_choice = input("Rock, Paper, or Scissors?: ").capitalize()
        if users_choice in ["Rock", "Paper", "Scissors"]:
            return users_choice
        else:
            print("Thats not part of the options! Please choose Rock, Paper, or Scissors :).")

def get_computers_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(users_choice, computers_choice):
    if users_choice == computers_choice:
        return "It's a tie!"
    elif (
        (users_choice == "Rock" and computers_choice == "Scissors") or
        (users_choice == "Paper" and computers_choice == "Rock") or
        (users_choice == "Scissors" and computers_choice == "Paper")
    ):
        return f"You win, Great Job! {users_choice} beats {computers_choice}."
    else:
        return f"You lose, Better luck next time :( ! {computers_choice} beats {users_choice}."

def this():
    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        users_choice = get_users_choice()
        computers_choice = get_computers_choice()

        print(f"You chose: {users_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(users_choice, computers_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("See you later then!")
            break

this()
