num = input("input a number:")
i = 0
j = 0
if num.isdecimal():
    for x in range(0, int(num)):
        if x % 2:
            i = x + i
        else:
            j = x + j
    print("Sum of odd numbers=", i)
    print("Sum of even numbers=", j)
else:
    print("invalid number")
