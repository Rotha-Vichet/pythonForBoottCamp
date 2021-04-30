again = True

decode = ""
while again:
    print("Press 1 to encode")
    print("press 2 to decode")
    chNum = input()

    if chNum == "1":
        print("enter the string to decode: ")
        u_Input = input("")
        lowerChar = u_Input.lower()
        letter = "abcdefghijklmnopqrstuvwxyz"

        for char in lowerChar:
            decode += letter[(letter.find(char)+13) % 26]
        print(decode.upper())

        print("Do you want to continue? [Y/N]")
        ans = input()
        if ans == "N":
            break
        else:
            continue
    elif chNum == "2":
        print("Enter string to decode: ")
        u_Input = input("")
        lowerChar = u_Input.lower()
        letter = "abcdefghijklmnopqrstuvwxyz"

        for char in lowerChar:
            decode += letter[(letter.find(char)-13) % 26]
        print(decode.upper())

        print("Do you want to continue? [Y/N]")
        ans = input()
        if ans == "N":
            break
        else:
            continue
