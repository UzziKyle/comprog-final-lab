from os import system as sys
from time import sleep as sp


def get_credentials() -> list:
    return ["ComputerScience", "PSU88@"]

def login() -> None:
    credentials = get_credentials()

    for tries in range(3):
        try:
            sys('cls')
            username = input("Enter username: ").strip()

            if username == credentials[0]:
                break

            elif tries == range(3)[-1]:
                sys('cls')
                print("Limit has reached")
                exit()

            else:
                print("Invalid username, you have {} attempt(s) left".format(range(3)[-1] - tries), end="\r")
                sp(0.5)

        except ValueError:
            print("Invalid input", end="\r")
            sp(0.5)

    for tries in range(3):
        try:
            sys('cls')
            password = input("Enter password: ").strip()

            if password == credentials[1]:
                break

            elif tries == range(3)[-1]:
                sys('cls')
                print("Limit has reached")
                exit()

            else:
                print("Invalid password, you have {} tries left".format(range(3)[-1] - tries), end="\r")
                sp(0.5)

        except ValueError:
            print("Invalid input", end="\r")
            sp(0.5)


security_modes = {
    1: {
        "function": login,
        "name": "Log In",
    },
    2: {
        "function": quit,
        "name": "Exit",
    }
}


def run_security() -> None:
    while True:
        try:
            sys('cls')
            print("Security Menu:")

            for mode_num in security_modes:
                print("{} - {}".format(mode_num,security_modes[mode_num]["name"]))

            user_input = int(input("Enter mode num: ").strip())

        except ValueError:
            print("Invalid Input", end="\r")
            sp(0.5)

        except KeyError:
            print("Invalid Input", end="\r")
            sp(0.5)

        else:
            security_modes[user_input]["function"]() # Runs the chosen module
            break
