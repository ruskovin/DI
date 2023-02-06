import time

# Exercise 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# my_dict = dict(zip(keys,values))
# print(my_dict)


# Exercise 2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family = {}
family_members = int(input('enter the number of famliy members'))
for i in range(family_members):
    name = input("enter your name")
    age = int(input("Enter your age"))
    family[name] = age

total_price  = 0
for age in family.values() :
    if age<3:
        total_price +=0
    elif 3<= age <=12:
        total_price+=10
    elif age >12:
        total_price += 15
print(family)

print("the family will pay ${}".format(total_price))

# Exercise 3 Zara

# brand = {
#     "name": "Zara" ,
# "creation_date": 1975 ,
# "creator_name": "Amancio Ortega Gaona ",
# "type_of_clothes": ["men", "women", "children", "home"],
# "international_competitors":[ "Gap", "H&M", "Benetton"],
# "number_stores": 7000 ,
# "major_color": {
#     "France": "blue", 
#     "Spain": "red", 
#     "US": ["pink", "green"],
# }
# }

# brand["number_stores"] = 2

# print("The international competitors of zara are {} {} and {}".format(brand["international_competitors"][0],brand["international_competitors"][1],brand["international_competitors"][2]))

# brand["country_creation"] = "Spain"

# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")


# del brand["creation_date"]

# print("The last international competitor is {} ".format(brand["international_competitors"][-1]))

# print("major clothes colors in the Us are {} and {}".format(brand["major_color"]["US"][0],brand["major_color"]["US"][1]))


# print(len(brand.items()))

# print(brand.keys())

# more_on_zara = {
#     "creation_date" :1975,
#     "number_stores": 10000,
# }

# brand.update(more_on_zara)

# print(brand)



# Exercise 4 : Disney Characters

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}

# for item in enumerate(users):
#     x,y = item
#     disney_users_A[y] = x

# print(disney_users_A)

# disney_users_B ={}

# for item in enumerate(users):
#     a,b = item
#     disney_users_B[a] = b 

# print(disney_users_B)

# disney_users_C = {}

# srted_users = sorted(users)
# for item in enumerate(srted_users):
#     i,j = item
#     disney_users_C[j] = i
# print(disney_users_C)

# lst_w_i = [x for x in users if 'i' in x]
# disney_users_with_i={}

# for item in enumerate(lst_w_i):
#     x,y = item
#     disney_users_with_i[y] = x

# print(disney_users_with_i)


# lst_w_m_or_p = [y for y in users if y[0]=='M' or y[0]=='P']


# disney_users_with_m_or_p={}
# for item in enumerate(lst_w_m_or_p):
#     x,y = item
#     disney_users_with_m_or_p[y] = x

# print(disney_users_with_m_or_p)

# start = time.time()
# name = "Leonardono"

# for l in range(len(name)):
#     if l == name.find('o', name.find("o")+1):
#           break
#     print(name[l], end="")

# end = time.time()
# print('\n')
# print(start - end)


# while True:
#     s = input("enter something")
#     if "quit" in s:
#         break
#     if len(s)<3:
#         print("too small")
#         continue
#     print("input is of sufficient length")

