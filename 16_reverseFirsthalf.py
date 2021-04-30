s = str(input("input a string:"))
s_first = s[0:len(s)//2]
s_second = s[len(s)//2 if len(s)%2 == 0
                            else ((len(s)//2)+1):]
if s == "":
    print("the string is empty.")
else:
    print(s_first[::-1], end="")
    print(s_second)
