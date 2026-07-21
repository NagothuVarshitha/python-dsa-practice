#Write a program to find the greatest of four numbers entered by the user
n=list(map(int,input("Enter a number: ").split()))
maxi=float('-inf')
for i in n:
    if i>maxi:
        maxi=i
print(maxi)