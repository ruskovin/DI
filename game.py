import random 
dc ={'win':0, 'lose':0, 'drew':0}
class Game():
    items = ['rock','paper','scissors']
    def get_user_item(self):
        user_item = input("please choose an item between: 'rock', 'paper' and 'scissors'")
        while user_item not in self.items:
            user_item = input("please choose an item between: 'rock', 'paper' and 'scissors'")
        return user_item


    def get_computer_item(self):
        computer_item = random.choice(self.items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == 'paper' and computer_item== 'rock':
            return 'win'
        elif user_item == 'rock' and computer_item ==  'scissors':
            return 'win'
        elif user_item == 'scissors' and computer_item ==  'paper':
            return 'win'
        elif user_item == computer_item:
            return 'drew'
        else:
            return 'lose'
    

    def play(self):
        usr =self.get_user_item()
        com = self.get_computer_item()
        res = self.get_game_result(usr,com)
        dc[res] += 1
        print(f"you selected {usr}, the computer selected {com}. You {res}")
        print(dc)
