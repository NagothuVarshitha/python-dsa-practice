n=int(input("Enter a number: "))
if n%400==0 or n%4==0 and n%100!=0:
        print("Leap Year")
else:
    print("Not Leap Year")