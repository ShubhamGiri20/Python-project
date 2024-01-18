from Words import word
import random
import string

def get_valid_word(word):
    w = random.choice(word) 
    while '-' in w or ' ' in w:
        w = random.choice(word)
    return w.upper()

def hangman():
    w = get_valid_word(word)
    word_letters = set(w)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print("You have used these letters: ",' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in w]
        print('Current words: ',' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used tha char. please try again.")
        else:
            print("Invalid charachter") 
    print(f"Yay you have guessed the word correctly {w}")

hangman()