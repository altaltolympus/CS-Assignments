def numCheck(text):
    while not text.isnumeric():
        text = input("hold up there you need to input numbers round these parts\n > ")
    return int(text)

def ynCheck(text):
    if text.lower() == ("y"):
        return True
    elif text.lower() == ("n"):
        return False
    else:
        text = input("what did you say\n> ")
    if text.lower() != "y" or "n":
        ynCheck(text)
bagCost = 223
orderCost = 0
discount = 0
bags = numCheck(input("so how many bags you want\n > "))
gold = ynCheck(input("now are you a GOLD CUSTOMER? GOLD CUSTOMERS get a 3.5% discount on all purchases! Sing up today to become a GOLD CUSTOMER! (y/n)\n > "))
orderCost = bagCost * bags
if bags > 99:
    discount = 10
elif bags > 24:
    discount = 5
if gold:
    discount += 3.5
orderCost -= orderCost * discount
print(f"your order costs €{orderCost / 100}have a nice day")