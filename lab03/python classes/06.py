class MyClass:
    def __init__(self, items):
        self.items = items

    def filter (self):
        self.items = list(filter(lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)), self.items))
        print(self.items)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ob = MyClass(my_list)
ob.filter()