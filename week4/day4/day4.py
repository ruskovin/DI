def hi(name , age):
    print("Hi I'm {} and I'm {} years old".format(name.title(), age))

hi("paul", 30)

#------------------------------------------------------
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

#------------------------------------------------

# def calculation(a,b):
#     return(f"a+b = {a+b}", f"a-b = {a-b}")

# res =(calculation(1,5)) 
# print(res)

#------------------------------------------------

# def greet_users(users):
#     for user in users:
#         print("Hello {}!".format(user.title()))

# names = ["paul", "laetitia" ,"james","sara"]
# greet_users(names)


# -----------------------------------------------------

# def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
#     print()
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#     return required_arg

# check_arguments_keywordedarguments("required argument")
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)

# -------------------------------------------------------------

# Passing *args and **kwargs as arguments

def check(a, b, c):
    print(a, b, c)

a = [1,2,3]
check(*a)
a = {'a':'Sarah', 'b': 24}
check(**a)
a = {'a':'Sarah', 'b':24, 'c': 180}
check(**a)

