def sugar():
    print("Hello, my friend")

def sugar2(name):
    print(f"Hello, {name}")
    print("Hello", name) 

sugar()
sugar2("Miracle")

def addition(a, b):
    return a + b

add = addition(28, 42)
print(add)

def add1 (a, b):
    return a + b

add = add1 (15, 25)
print(add)

def multiply1 (x, y):
    return x * y

multiply = multiply1 (4, 5)
print(multiply)

def square1(num):
    return num * num

square = square1 (6)
print(square)