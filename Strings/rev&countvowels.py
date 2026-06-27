t=input("Enter: ").strip()  #enter text
w=t.split() #split text into words w
res=[]  #store the result in res with "[]" as o/p is string instead of '0'
for i in w: #i goes through each word
    res.append(i[::-1])     #reverse each letter in word and append it to result
v=0     #initialize vowels
c=0     #initialize consonants
for ch in t:    #ch goes through text to count vowels and consonants
    if ch.isalpha():
        if ch.lower() in "aeiou":   #check if text is lower and vowels
            v+=1        #increment each count of vowel
        else:
            c+=1        #else increment each count of consonants
print("result:", " ".join(res))     #" " gives space between 2 words and .join combines elemnet(olleh dlrow) instead of ["olleh", "dlrow")
print("Vowels:",v)
print("consonants:",c)