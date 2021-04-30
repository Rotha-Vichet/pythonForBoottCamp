import random
randomNum = random.randint(2000, 3000)
n = int(input("input number:"))
i = 1
sum = 0

while i <= n:
        i += 1
        sum += randomNum

print("sum of even random number is:", sum)
