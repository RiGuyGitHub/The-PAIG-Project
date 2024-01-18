import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(1)
    print("Do you want to enter the cave? (yes/no)")

def cave():
    print("You enter the cave and it is dark inside.")
    time.sleep(1)
    print("You have two paths: a) go left or b) go right.")
    choice = input("Choose a or b: ").lower()

    if choice == 'a':
        print("You encounter a giant spider! What do you do?")
        time.sleep(1)
        print("a) Fight the spider")
        print("b) Try to run away")

        action = input("Choose a or b: ").lower()
        if action == 'a':
            print("You fight bravely but get bitten by the spider. Game Over!")
        elif action == 'b':
            print("You manage to escape the spider. Well done!")

    elif choice == 'b':
        print("You find a treasure chest. Do you want to open it? (yes/no)")
        open_chest = input().lower()
        if open_chest == 'yes':
            print("Congratulations! You found a treasure!")
        elif open_chest == 'no':
            print("You decide not to open the chest. The game continues.")

    else:
        print("Invalid choice. Please choose a or b.")
        cave()

def main():
    introduction()
    choice = input().lower()

    if choice == 'yes':
        cave()
    elif choice == 'no':
        print("You decide not to enter the cave. Game Over!")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        main()

if __name__ == "__main__":
    main()
