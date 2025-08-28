print("Hello world")
print("Welcome to python programmer")
name = "Miracle Chinaka"
age = 20
city = "Port Harcourt"

print(f"My name is {name}, I am {age} years old, and I live in {city}.")
# 2. Swap values of two variables without using a third variable
x = 10
y = 20
print("Before swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)
# 3. Take two numbers as input and print sum, difference, product, and quotient
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("Difference:", first_number - second_number)
print("Product:", first_number * second_number)

# To avoid ZeroDivisionError
if second_number != 0:
    print("Quotient:", first_number / second_number)
else:
    print("Quotient: Cannot divide by zero")

# 4. Take a string input, convert it to uppercase, and print
user_string = input("Enter a string: ")
print("Uppercase:", user_string.upper())
#ASSIGNMENT
# Write a code that can slice through a list of 10 programming languages.
# Rewrite that same code using a Tuple
# Attempt slicing the Tuple like you sliced the List
programming_languages = [
    "Python", "Java", "C", "C++", "Ruby", "JavaScript", "HTML", "CSS", 
    "SQL", "PHP", "Swift", "Kotlin", "Rust", "Go", "Perl", "MATLAB", 
    "TypeScript", "Bash", "PowerShell", "Lua"
]

print(programming_languages)
print(programming_languages[0:20])  
programming_languages = (
    "Python", "Java", "C", "C++", "Ruby", "JavaScript", "HTML", "CSS", 
    "SQL", "PHP", "Swift", "Kotlin", "Rust", "Go", "Perl", "MATLAB", 
    "TypeScript", "Bash", "PowerShell", "Lua" 
)

print(programming_languages)
print(programming_languages[0:20])


