# number = int(input('enter a number please'))
# length = int(input('enter a number please'))

# lst = [number*i for i in range(1,length+1)]
# print(lst)


# Challenge 2

user_word = input("enter a word please. duplicate letters will be removed")

word_without_duplicates = ""

for letter in user_word:
    if letter not in word_without_duplicates:
        word_without_duplicates += letter

print(word_without_duplicates)