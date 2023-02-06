my_dict ={}
word = input("Please enter a word")

for idx,letter in enumerate(word):
    if letter not in my_dict.keys():
        my_dict[letter] = []
    my_dict[letter].append(idx)

print(my_dict)