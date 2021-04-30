name = input("Input your name:")
time = int(input("Input the number of time to print:"))

if name.isalpha():
    for i in range(time):
        print(name)
else:
    print("no name enter")
