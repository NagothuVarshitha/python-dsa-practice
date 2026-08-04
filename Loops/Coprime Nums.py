"""Two numbers are called Coprime Numbers if their HCF is 1.
They don't have any common factor except 1.
Input-8 15
Factors of 8--1 2 4 8
Factors of 15--1 3 5 15
Common factor-1, HCF=1
Output-Coprime Numbers"""


n1,n2=map(int,input("Enter two numbers: ").split())
hcf=1   # Assume HCF is 1 initially
for i in range(1,min(n1,n2)+1): # Check every possible factor
    if n1%i==0 and n2%i==0: # If i divides both numbers, then it is a common factor
        hcf=i   # Store the latest (largest) common factor
if hcf==1:  # If HCF is 1, they are Coprime
    print("Coprime Number")
else:
    print("Not Coprime Number")