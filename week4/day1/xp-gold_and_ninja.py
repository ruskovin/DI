#Exercise 1
# print("Hello world\n"*4 +"I love python\n"*4)


# Exercise 2

# month = int(input("please enter the number of a month(1 to 12)"))

# if 3<= month <=5:
#     print("Spring")
# elif 6<= month <=8:
#     print('Summer')
# elif 9<= month <=11:
#     print('Autumn')
# elif month == 12 or month <=2:
#     print('Winter')


# Exercise 4 (how many characters in a sentence)

# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laboru"

# char_count = 0

# for char in my_text:
#     char_count +=1

# print(char_count)

# exercise 5 : Longest sentence without the letter 'a'

sentence = input("enter a sentence without the letter a  ")
longest = ''

for i in range(20):
    if 'a' in sentence:
        print("there's an a in the sentence try again")
    if not 'a' in sentence and (len(sentence) > len(longest) or len(sentence) == len(longest)) :
        print("Congratulations this word is the longest without an 'a'")
        longest = sentence[:]
    if (not 'a' in sentence) and len(sentence) < len(longest):
        print("that's good , continue")
    sentence = input("enter a sentence without the letter a  ")