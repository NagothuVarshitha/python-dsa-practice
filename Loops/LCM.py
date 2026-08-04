"""Least Common Multiple: The smallest number that is divisible by both given numbers.
The big number (lcm)
tries to get divided-->by both numbers
write hcf code as we know hcf value we can easily find lcm value through formula"""

n1,n2=map(int,input("Enter a number: ").split())
hcf=1
for i in range(1,min(n1,n2)+1): # Find the HCF
    if n1%i==0 and n2%i==0: # Check whether i divides both numbers
        hcf=i  # Store the latest common factor
lcm=(n1*n2)//hcf    # Apply the LCM formula
print(lcm)