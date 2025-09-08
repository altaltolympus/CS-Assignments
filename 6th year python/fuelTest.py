pollution = {
    "low": "wow how green of you",
    "medium": "i mean it's okay. could be better. not that great really",
    "high": "YUCKYYY EWWW"
}
def fuelCheck(text):
    if text == "diesel":
        return pollution["high"]
    elif text == "petrol":
        return pollution["medium"]
    elif text == "hybrid":
        return pollution["low"]
    else:
        text = input("what did you say.\n> ")
        fuelCheck(text)
age = int(input("how old is your car\n> "))
if age > 9:
    print(pollution["high"])
else:
    fuel = input("what fuel does your car use (diesel/petrol/hybrid)\n> ")
    print(fuelCheck(fuel))