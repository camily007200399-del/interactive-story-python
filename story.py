def start_story():
    print("You wake up in a strange place.")
    print("There are two paths ahead.")
    choice = input("Do you go left or right? ")

    if choice.lower() == "left":
        left_path()
    elif choice.lower() == "right":
        right_path()
    else:
        print("Invalid choice.")
        start_story()

def left_path():
    print("You find a quiet forest.")
    print("You feel safe. End of the story.")

def right_path():
    print("You find a dark cave.")
    print("Something moves inside... End of the story.")

start_story()
