def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)

def fun(*args):
    print(args)

fun(12,23,23)

def display(**kwargs):
    for i in kwargs:

        print(i)
        

display(emp="Kelly", salary=9000)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)


def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    return first_value

print(some_thing(13, 10))

def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    temp_value = other_thing(second_value)
    return temp_value

def other_thing(another_value):
    return (another_value + 5) * 3

print(some_thing(13, 10))

def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    temp_value = other_thing(second_value)
    return temp_value

def other_thing(another_value):
    return (another_value + 5) * 3

some_thing(13, 10)
# print(second_value)

def surprising_function(value):
    thing = 0
    for counter in range(value+1):
        thing = thing + counter
    return thing

print(surprising_function(5))

def a(x, y):
    x = x + 3
    y = y + 2
    return x+y

x = 5
y = 10
z = a(x, y)

print(z)

x = 67
if x != 67:
     print("x is not equal to 67")
else:
      print( 'x is equal to 67')

# func = lambda x: return x
# print(func(2))

print((lambda x: (x + 3) * 5 / 2)(3))

lst = ["name", "age"]

func = lambda x: ' '.join(x)(lst)
func
