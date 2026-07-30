"""A number is called an Automorphic Number if its square ends with the same number.
Input: 5
Square = 25
25 ends with 5
Output:Automorphic Number"""

n=int(input("Enter a number: "))
temp=n
square=n*n  # Find the square of the number
digit=len(str(n))   # Count how many digits are in the number
divisor=10**digit   # Create the divisor--# 1 digit -> 10,# 2 digits -> 100....
last_digit=square%divisor   # Get the last digits of the square
if temp==last_digit:    # Compare them with the original numbe
    print("Automorphic Number")
else:
    print("Not Automorphic Number")

