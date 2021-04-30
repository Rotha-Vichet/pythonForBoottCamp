num = input("input a number:")
sum_i = 0
sum_j = 0
countEven = 0
countOdd = 0
if num.isdecimal():
    for x in range(0, int(num)+1):
        if x % 2:
            sum_i += x
            countEven += 1
            aver_even = sum_i/countEven
        else:
            sum_j += x
            countOdd += 1
            aver_odd = sum_j/countOdd
    print("Sum of odd numbers=", aver_odd)
    print("Sum of even numbers=", aver_even)
else:
    print("invalid number")
