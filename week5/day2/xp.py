# Exercise 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     pass

# ben = Bengal('luc', 2)
# cha = Chartreux('audi', 3)
# sia = Siamese('drio', 5)

# all_cats = [ben,cha,sia]

# sara_pets = Pets(all_cats)

# sara_pets.walk()


# Exercise 2 Dogs

class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.speed = (self.weight/self.age)*10

    def bark(self):
        print(f"{self.name} is barking")
    
    def run_speed(self):
        print(f"running speed {self.speed}")
    
    def fight(self, other_dog):
        if (self.speed * self.weight) > (other_dog.speed * other_dog.weight) :
            print(f"{self.name} won")
        elif (self.speed * self.weight) < (other_dog.speed * other_dog.weight):
            print(f"{other_dog.name} won")

skip = Dog('skip',5, 20)
scooby = Dog('scooby', 8, 16)
dungo = Dog('dungo', 3, 13)

skip.fight(dungo)

scooby.fight(dungo)
