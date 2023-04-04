def my_function(a=1, b=2, c=3):
    print(a, b, c)


# my_function()
# my_function(4, 5, 6)
# my_function(a=7, c=8)

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3))
# print(add(1, 4))

def calculate(n, **kwargs):
    # print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=4)