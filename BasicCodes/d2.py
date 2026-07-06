"""6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
use key as their names. Assume that the names are unique.
formula: dictionary[key] = value
"""

d={}
for i in range(4):
    name=input("Enter name: ")
    language=input("Enter language: ")
    d[name]=language        #Store the value (language) using the key (name). -- dictionary[key] = value
                            #if the key occurs 2 times then the second one will be printed.
print(d)