"""HCF/GCD--The biggest number(factor) that divides both numbers completely.
Input: 12 18
Factors of 12: 1 2 3 4 6 12
Factors of 18: 1 2 3 6 9 18
Common factors: 1 2 3 6
Highest Common Factor = 6"""
#HCF can never be greater than the smaller n.o of i/p.

n1,n2=map(int,input("Enter a number: ").split())
hcf=1   #every +ve num have 1 as a common factor
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:       # If remainder is 0 for both numbers, then 'i' is a common factor.
        hcf=i   #Stores the latest common factor(we don't write hcf += i becoz we don't want factors sum(1+2+3+6)❌ we want the last stored value will be the Highest Common Factor(6).
print(hcf)

