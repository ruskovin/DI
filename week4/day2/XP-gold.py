import random
# Exercise 1

# a = ['apple', 'banana']
# b = ['strawberry','orange']

# a.extend(b)
# print(a)

# Exercise 2

# for i in range(1500, 2501):
#     if i % 5 ==0 and i % 7 ==0:
#         print(i)

# Exercise 3 Check the index

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# username = input("Enter your name please: ")

# if username in names:
#     print(names.index(username))


# Exercise 4: Greatest number

# a = int(input("enter a number "))
# b = int(input("enter a number "))
# c = int(input("enter a number "))
# lst = [a, b, c ]

# print(max(lst))

# Exercise 5 : The Alphabet

# alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
# 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# vowels = ['a', 'e', 'u', 'i', 'o', 'y']

# for i in alphabet:
#     if i in vowels:
#         print("{} is a vowel".format(i))
#     else :
#         print("{} is a consonant".format(i))


# Exercise 6 Words and letters

# ask = input("enter 7 words separated by space ")

# words = ask.split(" ")
# print(words)
# user_letter = input("Enter a letter please")

# for word in words:
#     for letter in word:
#         if letter == user_letter:
#             print(" the index of {} in {} is {}".format(user_letter,word,word.index(letter)))
#     if user_letter not in word:
#         print("not {} in {}".format(user_letter, word))

# Exercise 7 

# one_million_list =[x for x in range(1,1000001)]
# print(min(one_million_list))
# print(max(one_million_list))
# print(sum(one_million_list))

# Exercise 8 List and tuple

# csn = 34,67,55,33,12,98

# lst = []
# for i in csn:
#     lst.append(i)
    
# tle = tuple(lst)
# print(lst)
# print(tle)


# Exercise 9 : Random number
computer_number = random.randint(1, 9)

while True:
    usernum = int(input("please enter a number from 1 to 9 or ente '0' to quit "))

    if usernum == 0:
        print("okay See you next time")
        break
    if usernum == computer_number:
        print("Winner")
        break
    elif usernum != computer_number:
        print("better luck next time")