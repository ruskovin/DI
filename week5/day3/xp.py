# Exercise 2

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    def __str__(self):
        return (f"{self.amount} {self.currency}s")
    def __int__(self):
        return self.amount
    def __repr__(self):
        print("hello world")
        return (f"{self.amount} {self.currency}s")
    def __add__(self, other):
        if self.currency == other.currency:
            return int(self.amount) + int(other.amount)
        else:
            raise TypeError("currency not match")
        # return self.amount + other



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + c2)
c1 += c2
print(c1)
print(c1 + c3)