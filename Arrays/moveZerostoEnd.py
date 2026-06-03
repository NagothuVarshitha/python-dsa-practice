def movezerostoend(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr=[1,0,3,0,12]
print(movezerostoend(arr))