#class solution: creates a class.
#A class is like a mobile phone design.
#Functions are features inside phone.
#def twosum(self, nums, target): creates a function named twosum.
#Parameter	Meaning
#self	current object
#nums	array/list
#target	required sum
#1st loop moves through array indexes.
#nums = [2,7,11,15]
#length - len(nums) = 4
#range(4) - 0,1,2,3
#Second loop starts AFTER i, Because:We don't want same element twice.
#Check whether sum equals target.
#obj = solution() - Create object of class.
#result = obj.twosum([2,7,11,15], 9) - Call function


#class solution:
    #def twosum(self, nums, target):
       # for i in range(len(nums)):
           # for j in range(i+1, len(nums)):
              #  if nums[i]+nums[j]==target:
                 #   return [i,j]
#obj=solution()
#result=obj.twosum([2,7,11,15], 9)
#print(result)

arr = list(map(int,input("Enter: ").split()))
target = int(input("Enter:"))
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            target+=1
            print([i, j])
            break