def degree(x):
    y = 2
    def degree_two():
        return y ** x

    return degree_two()

print(degree(4))

def message(x):
    def print_message(y):
        return x, y

    return print_message

d = message(4)
a = message
print(d)
print(a)
print(d(10))

def adder(start_value):

    def inner(income):
        return start_value + income

    return inner

inner_add = adder(2)

adder = inner_add(10)

print(adder)


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
r = counter()
print(q())
q()
print(q())
print(r())

def my_func(x):
    def inner(y):
        return y * 2

    return x + inner(x)


print(my_func(15))
