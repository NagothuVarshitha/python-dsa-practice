#program to sum a list with 4 numbers.
l1=[]               #dont use list or sum as variables as they are built in so use l1 or total
total=0
for i in range(4):
    num=int(input("Enter a number: "))
    total+=num      #if i write sum=sum+i it gives 6 (as it adds indexs) so keep num to add nums
print(total)
