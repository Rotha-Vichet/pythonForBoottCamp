sum = 0

while True:
    number = input("enter a number:")
    if number != "stop":
        if number.isdecimal():
            number = int(number)
            sum += number
        else:
            print("please input valid number")
    else:
        print(f"The sum number is ", sum)
        break
