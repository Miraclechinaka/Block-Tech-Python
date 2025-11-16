def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

#Write a function that returns the square of a number
def square(num):
    return num * num
print(square(7))    
print(square(10))
print(square(15))

#Modify it to return the cube
def cube(num):
    return num ** 3
print(cube(7))
print(cube(10))
print(cube(15))

# Write a function that checks if a number is even
def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))
print(is_even(10))
print(is_even(15))
print(is_even(22))

#Return True for even numbers, False otherwise
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
print(is_even(10))
print(is_even(15))
print(is_even(22))


#Create a function that returns the last character of a string
def last_character(string):
    return string[-1]
print(last_character("Miracle"))
print(last_character("Python"))
print(last_character("Programming"))

 #If the string is empty, return "Empty!".
def last_char(text):
    if text == "":
        return "Empty!"
    return text[-1]
print(last_char("Miracle"))
print(last_char(""))

#Write a function that adds two numbers
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(5, 10))
print(add_two_numbers(20, 30))

#Add a third optional parameter.
def add_numbers(a, b, c=0):
    return a + b + c
print(add_numbers(5, 10))
print(add_numbers(5, 10, 15))
print(add_numbers(1, 2, 3))

#5. Write a function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(25))   # 77.0