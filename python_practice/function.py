def sugar():
    print("Hello, my friend") # function with no parameter/argument

def sugar2(name):
    print(f"Hello, {name}")
    print("Hello", name) 

sugar()
sugar2("Miracle")

def addition(a, b): # function with two parameters/arguments
    return a + b

add = addition(28, 42)
print(add)

def add1 (a, b):
    return a + b

add = add1 (15, 25)
print(add)

def multiply1 (x, y): # function with two parameters/arguments
    return x * y

multiply = multiply1 (4, 5)
print(multiply)

def square1(num):
    return num * num

square = square1 (6)
print(square)

def greete (surname = "Miracle Chinaka"):
    print(f"my surname is , {surname}")

greete() # to get the default value
greete(surname = "Jackson") # to get the first name/function parameter override the default value

# Function with multiple or abitrary arguments
def add9(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

result = add9(5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print(result)

# Function with multiple keyword arguments
def introduce(**details):
    for key, value in details.items():
        print(f"{key}: {value}")    
introduce(name="Miracle Chinaka", age=20, city="Port Harcourt", profession="Student", hobby="Reading")

