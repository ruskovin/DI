# Exercise 1 Formula

# C = 50
# H = 30
# D =0
# Q = ((2 * C * D)/H)**0.5

# ask = input("enter comma separated numbers")

# ask_list_str = ask.split(",")

# ask_list_int = [int(x) for x in ask_list_str]

# for i in ask_list_int:
#     print(int(((2 * C * i )/H)**0.5))

# Exercise 2 List of integers

#1
# lst = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 3]

#2 list , sorted in descending order list and sum of the numbers
# srted_lst = sorted(lst, reverse=True)
# print(lst)
# print(srted_lst)
# print(sum(lst))

#3 first and last numbers of the list 
# first_and_end_lst = [ lst[0], lst[-1]]

#4 list of numbers greater then 50
# great_fifty = [x for x in lst if x>50]
# print(great_fifty)

#5 list of numbers smaller than 10
# less_ten = [x for x in lst if x<10]
# print(less_ten)

#6 squared numbers list
# squared_lst = [x**2 for x in lst]
# print(squared_lst)

#7 without duplicates

# without_duplicates = []

# for i in lst:
#     if i not in without_duplicates:
#         without_duplicates.append(i)
# print(without_duplicates)

#8 average
# print(sum(lst)/len(lst))

#9 the largest number
# print("the largest number is {}".format(max(lst)))

#10 the smallest number
# print("the smallest number is {}".format(min(lst)))

#11 find the sum , average , largest and smallest number without built-in functions

# sm = 0
# length = 0

# for i in lst:
#     sm += i
#     length+=1
# print("The average is {}".format(sm/length))

# largest = 0

# for i in lst:
#     if i>largest:
#         largest = i
# print("The largest number is {}".format(largest))

# smallest = lst[0]

# for i in lst:
#     if i<smallest:
#         smallest=i

# print("The smallest number is {}".format(smallest))

# to be continue.....




# Exercise 3 : Working On A paragraph

# p = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."

# print("this paragraph contains {} characters".format(len(p)))

# print("there are {} sentences in the paragraph".format(p.count('.')))

# lst_p = p.split(" ")
# print("there are {} word in this paragraph".format(len(lst_p)))

# unique_words = []

# for i in lst_p:
#     if i not in unique_words:
#         unique_words.append(i)
# print("there are {} unique words in this paragraph".format(len(unique_words)))

# to be continue


# Exercise 4

user = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"

user_lst= user.split(" ")
user_lst_no_dupiclates = []
for word in user_lst:
    if word not in user_lst_no_dupiclates:
        user_lst_no_dupiclates.append(word)
for i in user_lst_no_dupiclates:
    ct = user.count(i)
    print("{} :{}".format(i, ct))




