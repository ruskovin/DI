from string import ascii_lowercase

# Exercise 1 Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('minou', 5)
# cat2 = Cat('loulou', 1)
# cat3 = Cat('skip', 3)

# cats = [cat1,cat2,cat3]

# def find_oldest_cat(a):
#     name_of_the_oldest_cat = ''
#     age_of_the_oldest_cat = 0

#     for cat in a:
#         if cat.age > age_of_the_oldest_cat:
#             name_of_the_oldest_cat = cat.name
#             age_of_the_oldest_cat = cat.age
#     return name_of_the_oldest_cat , age_of_the_oldest_cat


# oldest_name,oldest_age = find_oldest_cat(cats)

# print("the oldest cat is {} and is {} years old".format(oldest_name,oldest_age))


# Exercise 2 : Dogs

# class Dog():
#     def __init__(self,name, height):
#         self.name = name
#         self.height = height
    
#     def bark(self):
#         print("{} goes woof!".format(self.name))
    
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")
    
# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog.name)
# print(sarahs_dog.height,'cm')
# sarahs_dog.bark()
# sarahs_dog.jump()


# Exercise 3 : Who's the song producer?

# class Song():
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
    
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

# stairway.sing_me_a_song()


# Exercise 4 : Afternoon At the zoo

class Zoo():
    def __init__(self,zoo_name):
        animals = []
        self.animals = animals
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print("The animals in the zoo are: ")
        for animal in sorted(self.animals):
            print(animal)
        print("")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold!")
        else:
            print("We don't have that animal")
        print("")
    
    def sort_animals(self):
        first_letters = []
        for animal in self.animals :
            if animal[0] not in first_letters:
                first_letters.append(animal[0])
        first_letters.sort()
        ls =[]
        for i in range(len(first_letters)):
            ls.append(list(filter(lambda x : x[0]== first_letters[i], self.animals)))
        self.groups = dict(enumerate(ls,start=1))
        print('animals grouped by alphabetical order: ',self.groups)
        print("")
    
    def get_groups(self):
        for key,value in self.groups.items():
            print('group',key,'->',value)

    def ramat_gan_safari(self):
        add= input("which animal would we add in the zoo?")
        self.add_animal(add.title())
        rem = input("which animal would we sell today?")
        self.sell_animal(rem.title())
        self.get_animals()
        self.sort_animals()
        self.get_groups()

    
park = Zoo('Waza Park')

park.animals = ['Elephant','Ape', 'Baboob','Bobo', 'Cat', 'Emu']

park.add_animal("monkey")
park.add_animal("mouse")
park.sell_animal("Elephant")
# park.sort_animals()
# park.get_animals()
# park.get_groups()
park.ramat_gan_safari()