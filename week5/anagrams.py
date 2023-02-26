from anagram_checker import *
from string import punctuation,digits

def spe_char_check(char):
    special_chars = list(punctuation)
    if char in special_chars:
        return True
    return False

running = True

while running:
    user_inp = input("(x or q) Exit\nInput a word:")
    user_inp_wtws = user_inp.strip()

    if user_inp in ('x' ,'q'):
        print("Goodbye! See you soon!")
        running = False

    elif any(i.isdigit() for i in user_inp_wtws) or any(spe_char_check(i) for i in user_inp_wtws):
        print("please enter a word with valid characters")
    
    elif len(user_inp_wtws.split(' '))>1:
        print("Please enter a single word")

    elif user_inp_wtws == '':
        print("please enter a word, you entered nothing")

    else:
        anagram = AnagramChecker()
        print("YOUR WORD :", user_inp_wtws.upper())
        if anagram.is_valid_word(user_inp_wtws):
            print("YEAH! This is a valid English word")
            if anagram.get_anagrams(user_inp_wtws) == False:
                print("no anagram found")
            else:
                print(f"Here is a list of anagrams of {user_inp_wtws.upper()} : {anagram.get_anagrams(user_inp_wtws)} \n")
