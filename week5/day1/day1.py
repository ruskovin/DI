class Dog():
    def __init__(self, name):
        self.name = name
        print("hello {}".format(self.name))
    def get_name(self):
        print('my name is {}'.format(self.name))

a = Dog('Paul')

a.get_name()
