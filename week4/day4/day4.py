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

def greet_users(users):
    for user in users:
        print("Hello {}!".format(user.title()))

names = ["paul", "laetitia" ,"james","sara"]
greet_users(names)
