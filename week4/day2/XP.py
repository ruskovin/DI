import numpy as np
# Exercise 1 Set

# my_fav_numbers = {10, 8}

# print(my_fav_numbers)
# my_fav_numbers.discard(2)

# print(my_fav_numbers)

# friend_fav_numbers = {5, 7}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercice 2 : Tuple

#no there's no way of adding numbers in a string apart modifying the set manually

#Exercise 3 : List

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)


# Exercise 4: Floats

# a = 1
# lst = []
# for i in range(1,9):
#     a += 0.5
#     lst.append(a)
# print(lst)

# b = list(np.arange(1,5.5,0.5))
# print(b)


# Exercise 5 

# for i in range(21):
#     print(i)

# for i in range(21):
#     if i %2 ==0:
#         print(i)


# Exercise 6 
# my_name = "paul"
# user_input = input("enter a name : IT must be my name 0:)")
# while user_input.lower() != my_name:
#     user_input = input("Enter my name ")


# Exercise 7 : Favorite fruits

# user_fruit = input("enter your fruits serparated by a space")

# lst = user_fruit.split(" ")
# print(lst)
# ask = input("enter a name of a fruit")

# if ask in lst:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")


# Exercise 8: Who ordered a Pizza?
# toppings =[]
# while True:
#     topping = input("enter a topping you'll like to add and then enter 'q' when finished   ")
#     print("You'll add {} in your pizza".format(topping))
#     toppings.append(topping)
#     print(toppings)
#     if topping == 'q':
#         print("the total price is {}{}".format('$',10+ 2.5*((len(toppings )-1))))
#         break


# Exercise 9 : Cinemax
# total_price = 0

# while True:
#     age = int(input("enter your age or enter 0 to exit"))
#     if age <3:
#         total_price+=0
#     elif 3 <= age <= 12 :
#         total_price +=10
#     elif age >12:
#         total_price +=15
#     if age == 0 :
#         break
# print(total_price)

# names = ['paul', 'sarah', 'jordan','mary']

# for name in names:
#     age = int(input("enter your age  " + name))
#     if 16<age<21:
#         names.remove(name)
# print(names)


# Exercise 10 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich","Sabih sandwich","Pastrami sandwich"]

sandwich_orders.extend(['Pastrami sandwich', 'Pastrami sandwich'])

print("Sorry the deli has run out of pastrami")

while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

print(sandwich_orders)

finished_sandwiches = []
for i in range(len(sandwich_orders)):
    finished = sandwich_orders.pop(0)
    finished_sandwiches.append(finished) 
    print("I made your {}".format(finished))

print(finished_sandwiches)

# Exercise 11 Sandwich orders 2

