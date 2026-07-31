"""Sunny Number if n + 1 is a perfect square.
Input: 8
8 + 1 = 9
√9 = 3
Output: Sunny Number"""
n=int(input("Enter a number: "))
new=n+1 #Add +1
found = False   # Assume it is not Sunny
for i in range(1,new+1):    # Check every number from 1 to new
    if i*i==new:    # Check whether i*i equals new
        found=True
        break
if found:
    print("Sunny Number")
else:
    print("Not Sunny Number")

