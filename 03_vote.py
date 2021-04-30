number = int(input("Input your age:"))

if number >= 0:
    if number >= 18:
        print("You are eligible to vote")
    else:
        print("You aren't adult yet... Sorry can't vote")
else:
    print("Age must be a positive digit")
