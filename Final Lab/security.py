# SECURITY FUNCTIONS AND MAIN PROGRAM CALL

# A function that asks for a username. 
def userNameAgain(n):
    username = input("\nEnter username again: ").strip()
    n

    if username == 'ComputerScience':
        getPassword(3)

    else:
        n = n - 1
        print("\nInvalid username")

        if n != 0:
            print("You have (",n,") tries left")
            userNameAgain(n)

        else:
            invalidUsername()


# A function that asks for a passcode. 
def getPassword(n):
    password = input("Enter password: ").strip()
    n

    # If passcode is correct, it'll import the main program.
    if password == "PSU88@":
        print('\n---------------------------------------------------')

    # Else, it stops the program.
    else:
        n = n - 1
        print("\nInvalid passcode")
 
        if n != 0:
            print("You have (",n,") tries left\n")
            getPassword(n)

        else:
            invalidUsername()

# Will be called if the input has reached its error limit
def invalidUsername():
    print("Sorry.")
    exit()

# StartUp - the start of the program, first attempt of asking the username
def askUsername():
    username = input("\nEnter username: ").strip()
    if username == 'ComputerScience':
        getPassword(3)

    else:
        print("\nInvalid username")
        print("You have (",2, ") tries left")
        userNameAgain(2)