import random as r
com_num = r.randint(1,10)
for i in range(3):
    choise = int(input("Enter the number: "))
    if (choise == com_num):
        print("You win")
        print(f"Number of chances {i+1}")
        break
    elif (choise > com_num):
        print("Enter lower number..")
        print(f"Chances left {2-i}")
    elif (choise < com_num):
        print("Enter bigger number..")
        print(f"Chances left {2-i}")
    else:
        print("You lose")
