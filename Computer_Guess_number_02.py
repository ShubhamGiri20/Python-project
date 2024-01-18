import random as r

def computer(x):
    low = 1
    high = x
    feedback = ''
    i = 0
    while feedback != 'c':
        if low != high :
            com_num = r.randint(low,high)
        else: 
            com_num = low
        feedback = input(f"Is the input {com_num} too high (h), too low (l) or correct (c): ").lower()
        if feedback == 'h':
            high = com_num - 1
        elif feedback == 'l':
            low = com_num + 1
        i = i + 1
    print(f"Congratulation, the computer has won and guessed the correct number {com_num} in {i} guesses.")

computer(100)