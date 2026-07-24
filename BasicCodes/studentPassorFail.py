n=list(map(int,input("Enter: ").split()))
avg=sum(n)/len(n)
passed=True
"""This is called a flag variable.
Initially, we assume:
"The student has passed all subjects.
If we later find any subject with marks less than 33, we'll change it to:
"""
for i in n:
    if i<33:
        passed=False    #It stays False until the end of the program
if avg>=40 and passed:
    print("Pass")
else:
    print("Fail")

    """if avg>=40 and passed:-----The student passes only if both conditions are true:
Average is 40 or more.
passed is True (meaning every subject has at least 33 marks)."""