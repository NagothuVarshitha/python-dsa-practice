"""A number is called a Happy Number if repeatedly replacing the number with
 the sum of the squares of its digits eventually becomes 1.
If it never becomes 1 and keeps repeating, it is Not a Happy Number.
Input: 19
Step 1: 1² + 9²= 1 + 81= 82
Step 2: 8² + 2²= 64 + 4= 68
Step 3: 6² + 8²= 36 + 64= 100
Step 4: 1² + 0² + 0²= 1
Output: Happy Number"""
n=int(input("Enter the number:"))
while n!=1: # Repeat until the number becomes 1
    temp=n   # Store the current number because n will become 0
    sum=0   # Variable to store the sum of squares of digits
    while temp>0:  # Find the sum of squares of digits
        rem=temp%10
        sum=sum+rem**2
        temp=temp//10
    if sum==4:  # If the number becomes 4, it will keep repeating forever(proof:If a number is not happy,Every unhappy number eventually reaches 4, then loops forever.)
        print("Not Happy Number")
        break
    n=sum    # Replace n with the new sum
if n==1:    # If the loop ended because n became 1
    print("Happy Number")
