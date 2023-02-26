
# EXERCISE 1

def find(lst):
    if lst.count(19) == 2 and lst.count(5)>=3:
        return True
    return False

ls1 =[19, 19, 15, 5, 3, 5, 5, 2]
ls2 =[19, 15, 15, 5, 3, 3, 5, 2]
ls3 =[19, 19, 5, 5, 5, 5, 5]

print(find(ls1))
print(find(ls2))
print(find(ls3))

# Exercise 3
def diff_three(lst):
    pairs = []
    for i in range(0,len(lst)):
        for j in range(i,len(lst)):
            if abs(lst[i] - lst[j]) == 3:
                pairs.append((lst[i],lst[j]))
    return pairs


lst1=[0, 3, 4, 7, 9]
lst2=[0, -3, -5, -7, -8]
lst3=[1, 2, 3, 4, 5]
lst4=[100, 102, 103, 114, 115]

print(diff_three(lst1))
print(diff_three(lst2))
print(diff_three(lst3))
print(diff_three(lst4))


# Exercise 4
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)

cache.put(10, 10)
cache.put(20, 20)
print(cache.get(10))   #10
cache.put(30, 30)       
print(cache.get(20))   #-1 
cache.put(40, 40)      
print(cache.get(10))   #-1 
print(cache.get(30))   #30
print(cache.get(40))   #40


# Exercise 5
print('***********************')
print('***********************')
print('***********************')


def find_pairs(lst, num):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst [j] == num:
                pairs.append((lst[i],lst[j]))
    return pairs

print(find_pairs(lst1, 10))
print(find_pairs(lst2, 10))
print(find_pairs(lst3, 10))