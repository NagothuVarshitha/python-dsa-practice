arr=[12,32,1,10,34]
max1=arr[0]
max2=arr[0]
for i in arr:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max2:
        max2=i
print("second largest:",max2)