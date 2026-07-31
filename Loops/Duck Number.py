"""number that contains at least one zero, but does not start with zero.
1023 → Duck Number
120 → Duck Number
321 → Not Duck Number"""
n=int(input("Enter a number: "))
if "0" in n and not n.startswith("0"):
        print("Duck Number")
else:
    print("Not Duck Number")