from xp import Dog
import random

class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained = False
    
    def train(self):
        self.bark()
        self.trained = True
    
    def play(self, *args):
        names_list = [dog.name for dog in args]
        names = ' '.join(names_list)
        print(f"{names} and {self.name} all play together")
    
    def do_a_trick(self):
        tricks = [f"{self.name} doess a barrel roll",
        f"{self.name} stands on his back legs",
        f"{self.name} shake your hand",
        f"{self.name} plays dead"]
        if self.trained:
            print(tricks[random.randint(0,3)])
        else:
            print("Dog not trained. Can't do tricks")
        


pet = PetDog('lion', 15, 11)
pet2 = PetDog('pluto', 11, 35)
pet3 = PetDog('dungo', 15, 24)
pet4 = PetDog('scooby', 20, 19)

pet.play(pet2,pet3, pet4)
pet.train()
pet.do_a_trick()