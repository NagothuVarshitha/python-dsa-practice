"""number that contains at least one zero, but does not start with zero.
1023 → Duck Number
120 → Duck Number
321 → Not Duck Number"""
n=input("Enter a number: ") #Take the input as a string, as startswith() works for str only and "0" is also a str
# Check if the number contains 0,and does not start with 0
if "0" in n and not n.startswith("0"):
    print("Duck Number")
else:
    print("Not Duck Number")
