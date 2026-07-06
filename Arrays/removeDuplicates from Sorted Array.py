nums=list(map(int,input("Enter: ").split()))
k=1 #Because the first element is always unique in a sorted array.
for i in range(len(nums)):
    if nums[i]!=nums[i-1]:  #we use this line when array is sorted, duplicates are together.
        nums[k]=nums[i]
        k+=1
print(k)


