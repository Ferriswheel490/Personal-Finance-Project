# Jacksons Essential Functions

def cs(): # Clears the screen
    print("\033c",end="")

def end(message): # Ends the program with an end message
    cs()
    print(message)
    quit()

def int_input(msg):
    while True:
        try:
            output = int(input(msg))
            break
        except ValueError:
            input("Invalid Input! (Only integers accepted)\nPress enter to continue")
    return output