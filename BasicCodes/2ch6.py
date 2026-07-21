"""find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject
to pass. Assume 3 subjects and take marks as an input from the user."""
n=list(map(int,input("Enter: ").split()))
total=sum(n)
percentage=total/3
if percentage>=40 and n[0]>33 and n[1]>33 and n[2]>33:
    print("Pass")
else:
    print("Fail")