s = str(input("input a string:"))
newStr = ""

for i in range(0, len(s)):

    if s[i].islower():
        newStr += s[i].upper()
    elif s[i].isupper():
        newStr += s[i].lower()
if s == "":
    print("the string is empty.")

print(newStr)
