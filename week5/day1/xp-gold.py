# import math
# import random
# # Exercise 1

# class Circle():
#     def __init__(self,radius=1.0):
#         self.radius = radius
#     def perimeter(self):
#         return (self.radius *2 * math.pi)
#     def area(self):
#         return(math.pi * (self.radius**2))
#     def geometry_def(self):
#         print("A circle is a round-shaped figure that has no corners or edges.")


# # Exercise 2

# class Mylist():
#     def __init__(self,lst):
#         self.lst = lst
#     def reverse(self):
#         return (self.lst[::-1])
#     def sorted(self):
#         return sorted(self.lst)
#     def rdm_lst(self):
#         random_lst = []
#         for i in range(len(self.lst)):
#             random_lst.append(random.randint(0,35))
#         return(random_lst)

# # Exercise 3

class MenuManager():
    def __init__(self):
        self.menu = [
            {
                "name": "Soup",
                "price": 10,
                "spice level":'B',
                "gluten": False,
            },
            {
                "name": "Hamburger",
                "price": 15,
                "spice level":'A',
                "gluten": True,
            },
            {
                "name": "Salad",
                "price": 18,
                "spice level":'A',
                "gluten": False,
            },
            {
                "name": "French Fries",
                "price": 5,
                "spice level":'C',
                "gluten": False,
            },
            {
                "name": "Beef bourguignon",
                "price": 25,
                "spice level":'B',
                "gluten": True,
            }
        ]
    
    def get_menu(self):
        return self.menu

    def add_item(self,name,price,spice,gluten):
        self.menu.append({"name":name, "price":price, "spice level":spice, "gluten":gluten})
    
    def update_item(self,name,price,spice,gluten):
        # for i in range(len(self.menu)):
        #     if self.menu[i]["name"] == name:
        #         self.menu[i]["name"] = name
        #         self.menu[i]["price"] = price
        #         self.menu[i]["spice level"] = spice
        #         self.menu[i]["gluten"] = gluten
        #         return
        for i in self.menu:
            if i["name"] == name:
                i["name"] = name
                i["price"] = price
                i["spice level"] = spice
                i["gluten"] = gluten
                return

        print("The dish is not in the menu")
    
    def remove_item(self,name):
        for i in range(len(self.menu)):
            if self.menu[i]["name"] == name:
                del self.menu[i]
                return
        print("the dish you want to delete is not in the menu") 

men = MenuManager()

men.update_item('Soup', 60, 'D',True)

men.add_item('food', 40, 'D',True)


print(men.get_menu())

        
