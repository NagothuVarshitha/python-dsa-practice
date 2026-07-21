"""A spam comment is defined as a text containing following keywords: “Make a lot of money”,
“buy now”, “subscribe this”, “click this”. Write a program to detect these spams"""
s=list(input("Enter: ").split())
text=input("Enter:")
for ch in s:
    if ch.lower() in text.lower():
        print("Detected spam")
        break
else:
    print("Not spam")
