import random

ask = input("enter a sentece of 10 characters   ")

length = len(ask)

if length < 10 :
    print("String not long enough")
elif length > 10:
    print("Sting too long")
elif length ==10 :
    print('the first character is ' + ask[0]+ " and the last character is "+ ask[-1])

line =''
for char in ask:
    line += char
    print(line)

line_shuffle =""

for char in ask:
    line_shuffle+= char
    d = list(line_shuffle)
    random.shuffle(d)
    print("".join(d))