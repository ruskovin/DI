import random

# # Exercise 1 what are you learning

# def display_message():
#     print("Hey! I'm learning python functions")

# display_message()


# # Exercise 2: What's your favorite book

# def favorite_book(title):
#     print("one of my favorite book is '{}'".format(title))

# favorite_book("the prince")

# # Exercise 3: Some Geography

# def describe_city(city, country='England'):
#     print(f"{city} is in {country}")

# describe_city('Yaounde', 'Cameroon')

# # Exercise 4: Random

# def guess(num):
#     computer_num = random.randint(1, 100)
#     if num == computer_num:
#         print("Winner")
#     else:
#         print("Sorry, try again!")

# # Exercise 5: Let's Create some personalized shirts!

# def make_shirt(size='Large', text="I love python"):
#     print("The size of the shirt is {} and the text is '{}'".format(size,text))

# make_shirt()
# make_shirt('medium')
# make_shirt("small", "Themistocle")
# make_shirt(size="any",text="hoorah")

# # Exercise 6 : Magicians

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(mag_list):
#     for mag in mag_list:
#         print(mag)
# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] = "The great {}".format(magicians[i])


# show_magicians(magician_names)
# make_great(magician_names)
# print(magician_names)


# Exercise 7: Temperature Advice

def get_random_temp(season):
    rdm_temp =0
    if season == 'winter':
        rdm_temp = random.randint(-10, 16)
    elif season =='autumn':
        rdm_temp = random.randint(17, 23)
    elif season =='spring':
        rdm_temp = random.randint(24, 31)
    elif season =='summer':
        rdm_temp = random.randint(32, 40)
    return rdm_temp

def main():
    s = input("enter a season please")
    rtemp = get_random_temp(s)
    if rtemp < 0 :
        print("Brr, that's freezing! Wear some extra layers today")
    elif 0 <= rtemp < 16 :
        print("Quite chilly! Don't forget your coat")
    elif 16 <= rtemp <= 23:
        print("wow realy good time")
    elif 24 <= rtemp < 32:
        print('a sunny day')
    elif 32 <= rtemp <=40:
        print("what a heat")
    print(f"the temperature right now is {rtemp}")

main()