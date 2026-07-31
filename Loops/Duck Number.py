"""number that contains at least one zero, but does not start with zero.
1023 → Duck Number
120 → Duck Number
321 → Not Duck Number"""
n=int(input("Enter a number: "))
temp=n
digit=str(n)
while n>0:
    if digit.endswith("0") and digit>=0:
        print("Duck Number")
    else:
        print("Not Duck Number")