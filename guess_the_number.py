import random
from colorama import Fore


def is_valid(number):
    is_valid_number = True

    if number.isdigit():
        number = int(number)

        if number < 1 or number > 100:
            is_valid_number = False
    else:
        is_valid_number = False
    return is_valid_number


cpu_num = random.randint(1, 100)
playing = True

while playing:
    player_input = input(Fore.CYAN + "Guess the number (1 - 100): ")

    if not is_valid(player_input):
        print(Fore.RED + "Invalid input. Write a number between 1-100")
        continue
    else:
        player_input = int(player_input)

    if player_input == cpu_num:
        print()
        print(Fore.GREEN + "Congrats! You have guessed the number!")
        print()

        play_again = input(Fore.CYAN + "Do you want to play again? Type [Y]es or [N]o: ")
        while True:

            if play_again == "Y":
                break
            elif play_again == "N":
                print(Fore.CYAN + "Thanks for playing!")
                playing = False
                break
            else:
                play_again = input(Fore.RED + "Invalid answer. Please, type [Y]es or [N]o: ")

    elif player_input < cpu_num:
        print(Fore.YELLOW + "Too low")
    else:
        print(Fore.YELLOW + "Too high")
