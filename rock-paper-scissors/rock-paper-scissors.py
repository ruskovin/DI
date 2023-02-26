from game import *

def get_user_menu_choice():
    global us_choice
    us_choice = input('choose an option:\n (p) Play a new game \n (s) Show scores \n (q or x) quit \n')

def main():
    running = True
    while running:
        get_user_menu_choice()
        if us_choice =='p':
            gme = Game()
            gme.play()
        elif us_choice =='s':
            print(dc)
        elif us_choice ==('q' or'x'):
            print(dc)
            running = False
main()