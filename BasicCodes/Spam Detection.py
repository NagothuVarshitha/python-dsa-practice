## List of spam words or take it from user
spam=["Make a lot of money",
    "buy now",
    "subscribe this",
    "click this"]
#Take input from the user
text=input("Enter your text: ")
result=[]
#Check each spam word one by one
for ch in spam:
    if ch.lower() in text.lower():  #Convert both to lowercase and check if the spam word exists
        print("Detected spam")
        break   # Stop checking further
else:   # Runs only if the loop finishes without break
    print("Not spam")