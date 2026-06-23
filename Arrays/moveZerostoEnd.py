#def movezerostoend(arr):  #Creates a function named movezerostoend that takes an array arr as input.
    #j=0     #j keeps track of the position where the next non-zero element should be placed.
   # for i in range(len(arr)):   #i goes from 0 to len(arr)-1.
       # if arr[i]!=0:       #Check for non-zero: Only process elements that are not zero.
           # arr[j],arr[i]=arr[i],arr[j]     #Swap:Move the non-zero element to position j.
         #   j+=1        #Move j to the next position for future non-zero elements.
    #return arr
#arr=[1,0,3,0,12]
#print(movezerostoend(arr))



n=int(input())  #Single number
arr=list(map(int,input().split())) #Array/List
j=0
for i in range(0,n):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
print(arr)