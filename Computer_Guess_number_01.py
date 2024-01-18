import random as r

def computer(x):
    choise = int(input("Enter the number for the computer to guess: "))
    i = 0
    while (x):
        com_choice = r.randint(1,x)
        if com_choice == choise :
            print("Computer has won...")
            print(f"Computer have won in {i} chances.")
            break
        elif com_choice != choise:
            i = i + 1
computer(100)