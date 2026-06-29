#Write a program to detect double space in a string.

s=input("Enter: ")
for ch in range(len(s)):
    if s[ch]==" " and s[ch+1]==" ":
        print("Double Space Found")