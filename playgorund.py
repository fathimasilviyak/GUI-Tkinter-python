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


print(add(1, 2, 3))
print(add(1, 4))