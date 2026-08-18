"""
A
A B
A B C
A B C D
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ") #j starts from 1, while A starts at ASCII/Unicode value 65. So we add 64 to shift 1 → 65, 2 → 66, etc.
    print()