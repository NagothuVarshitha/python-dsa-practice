n=int(input("Enter the number: "))
result=[]  #create an empty list and will store all answers.
for i in range(1,n+1):  #range() works with integers, not strings.
    if i%3==0 and i%5==0:
        result.append("FizzBuzz")
    elif i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(str(i))
print(result)