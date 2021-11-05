
valid = False

while valid == False:
    email = input("Enter a email: ")

    if "@" in email:
        if "." in email:
            print("It is a valid email.")
            valid = True
        else:
            print("It is not a valid email. Try again.")
            valid = False
    else:
        print("It is not a valid email. Try again")
        valid = False