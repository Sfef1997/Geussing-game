import random

def show_score(attempts_list):
    """
    Display the player's high score.

    Args:
        attempts_list (list): List of attempts for each game.

    Returns:
        None
    """
    if not attempts_list:
        print("There is No Currently Score, start playing")
    else:
        print(f"Your High Score is: {min(attempts_list)} attempts")

def give_hint(guess, random_num):
    """
    Provide a hint based on the player's guess and the randomly generated number.

    Args:
        guess (int): The player's guess.
        random_num (int): The randomly generated number.

    Returns:
        None
    """
    if guess != random_num:
        print("Too low" if guess < random_num else "Too high")

def play_game():
    """
    Play a single game of guessing the number.

    Returns:
        attempts_list (list): List of attempts for the current game.
    """
    attempts_list = []
    attempts = 0
    random_num = random.randint(1, 10)

    print("Hello Player, welcome to the guessing Game!")
    player_name = input("Insert your Name please.\n")
    wanna_play = input(
        f"{player_name}, do you Like To play\n"
        "(enter yes / No)"
    ).lower()

    if wanna_play == "no":
        print("That's cool, thanks")
        return attempts_list

    show_score(attempts_list)

    while wanna_play == "yes":
        try:
            guess = int(input("Pick a Number Between 1 and 10:\n"))
            if not 1 <= guess <= 10:
                raise ValueError("Please pick a number in the range 1-10")

            attempts += 1
            attempts_list.append(attempts)

            if guess == random_num:
                print("Nice, you got it!")
                print(f"It took you {attempts} attempts!")
                wanna_play = input("Would you like to play again? (Enter Yes / No)\n").lower()
                if wanna_play == "no":
                    print("That's cool, have a good day")
                else:
                    break
            give_hint(guess, random_num)
        except ValueError as error:
            print(error)

    return attempts_list

if __name__ == "__main__":
    while True:
        attempts_list = play_game()
        if input("Do you want to play again? (Enter Yes / No)\n").lower() != "yes":
            break
