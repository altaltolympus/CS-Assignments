def numCheck(text):
    while not text.isnumeric():
        text = input("hold up there you need to input numbers round these parts\n > ")
    return int(text)

score = numCheck(input("What was your test score?\n > "))

if score < 80:
    print("Please try harder next time.")
else:
    age = numCheck(input("how old.\n > "))
    if age < 17:
        print("Excellent :D")
    else:
        print("Good.")