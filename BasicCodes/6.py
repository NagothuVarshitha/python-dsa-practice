#Write a program to find the greatest of four numbers entered by the user
n=list(map(int,input("Enter :").split()))
maxi=n[0]       #n[0]:This works for positive, negative, and mixed numbers.
for i in n:
    if i>maxi:
        maxi=i
print("Greatest Number",maxi)

