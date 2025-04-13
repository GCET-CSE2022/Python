# Python Program for Compound Interest

def compoundInterest(principle,rate,time) :
    amount =   principle * (1 + rate / 100) ** time
    CI = amount - principle
    return CI

principle  = float(input("Enter the principal : \n"))
rate = float(input("Enter the Rate of interest : \n"))
time = float(input("Enter the time (years): \n"))

CompoundInterest = compoundInterest(principle,rate,time)
print("The Compound Interest is : \n",CompoundInterest)