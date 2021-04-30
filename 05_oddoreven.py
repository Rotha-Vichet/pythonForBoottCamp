number = input('Enter a number:')

if number.isdecimal():
    num = int(number) % 2
    if num == 0:
        print('The number you have entered is Even')
    else:
        print('The number you have entered is Odd')
else:
    print('Not a valid number')
