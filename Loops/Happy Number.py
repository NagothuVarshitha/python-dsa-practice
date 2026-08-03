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
