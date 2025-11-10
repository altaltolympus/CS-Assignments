def monthlyRepayment(p, i, t):
    f = p * (1 + i) ** t # F = P(1+i)^t
    m = f / (years * 12)
    return round(m, 2)

principal = int(input("How much money do you want to borrow?\n > "))
interest = float(input("How much interest will you pay as a percentage of this?\n > "))
years = int(input("Over how many years will you repay this laon?\n > "))
income = float(input("How much is your net monthly income?\n > "))
cutoff = float(input("Where is the cutoff point?\n > "))
application = monthlyRepayment(principal, interest, years)
success = False

if income * cutoff > application:
    success = True

print(f"Monthly repayments would be equal to {application}")
if success:
    print("Your application has been accepted!")
else:
    print("Your application has been rejected.")