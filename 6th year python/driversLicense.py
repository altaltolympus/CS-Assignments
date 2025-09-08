def ynCheck(text):
    if text.lower() == ("y"):
        return True
    elif text.lower() == ("n"):
        return False
    else:
        text = input("what did you say\n> ")
    if text.lower() != "y" or "n":
        ynCheck(text)
age = int(input("how old \n> "))
if age < 17:
    print("you are baby go home")
else:
    prov = ynCheck(input("provisional license? (y/n)\n> "))
    if prov:
        print("cool go get your license")
    if not prov:
        print("do you even know how to drive. no license for you")
    else:
        print("if you are reading this, i messed up somehow")