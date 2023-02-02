shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3001',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3002',
    'size': 'L',
    'price': 30
  },
]
# for i in shirts:
#     for key, value in i.items():
#         print(key,value)

# for i in range(len(shirts)):
#     for key,value in shirts[i].items():
#         print(key,value)




# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":"80"
#          }
#       }
#    }
# }
# print(sample_dict['class']["student"]["marks"]["history"])


# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]

# print(keys_to_remove)
# for key in keys_to_remove:
#     del sample_dict[key]+
# print(sample_dict)


for item in enumerate("abcd"):
    print(item)