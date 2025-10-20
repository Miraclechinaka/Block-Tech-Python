""""# while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # count = count + 1"""

x = 15
while x > 0:
    print("x is:", x)
    x -= 2  # this is equivalent to x = x - 2
    if x == 7:
        print("x is now 4, breaking the loop.")
        break
        if x == 9:
            continue
