s = str(input("input a string:"))
l = list(s)
if s == "":
    print("the string is empty.")
else:
    for i in s:
        print(i, ":", ord(i))

