# Essential Functions

def cs(): # Clears the screen
    print("\033c",end="")

def end(message): # Ends the program with an end message
    cs()
    print(message)
    quit()