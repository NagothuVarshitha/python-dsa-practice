"""Circular Prime Number if:Every rotation of its digits is also a Prime Number.
Input-197
rotation-->Move the first digit to the last.
(Trick:If a number has n digits, then it has n rotations.)
197-->971-->719------->rotation=3
✅for 197--->num[1:] + num[0]
"97" + "1"-->"971"
Output-Circular Prime Number"""

n=int(input("Enter number:"))
temp=str(n) # Convert number into string, If temp were an integer,so we convert to a string only for rotation
flag=True   # Assume the number is Circular Prime
for i in range(len(temp)):  # Repeat as many times as there are digits
    num=int(temp)   #before it is string(The % operator for prime checking needs an integer), so we convert it back.
    count=0 # Check whether this rotation is Prime
    for j in range(1,num+1):
        if num%j==0:
            count=count+1
    if count!=2:     # If any rotation is not Prime
        flag=False
        break
    temp=temp[1:]+ temp[0]   # Rotate the number,Move the first digit to the last
if flag:    # Print the result
    print("Circular Prime Number")
else:
    print("Not Circular Prime Number")





