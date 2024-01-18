import random as r

def guess(x):
    com_choise = r.randint(1,x)
    choise = 0
    while choise != com_choise:
        choise = int(input("Enter the number: "))
        if choise == com_choise:
            print("You Win....")
            break
        elif choise > com_choise:
            print("Wrong number.. Enter a little low number...")
        elif choise < com_choise:
            print("Wrong number.. Enter a little higher number...")

guess(100)