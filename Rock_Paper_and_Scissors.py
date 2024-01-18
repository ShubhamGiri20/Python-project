import random

def play():
    user = input("Enter your choice rock(r), paper(p) or scissor(s): ").lower()
    com = random.choice(['r','p','s'])
    if user == com:
        return 'Tie' 
    if is_win(user,com):
        return "You win..."
    return "You lose.."
def is_win(player , opponent ):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())