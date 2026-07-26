n=int(input("Enter: "))
result=[]   #Creates an empty list to store answers.
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        result.append("FizzBuzz")   #Adds one item to the list, instead of printing at a time
    elif i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(str(i))
print(result)   #Prints the complete list after all elements have been added.
