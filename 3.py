a=input("enter a string:")
vowels=0
consonants=0
for ch in a:
    if ch in'aeiouAEIOU':
        vowels+=1
    else:
        consonants+=1
print("NO. of vowels=",vowels)
print("NO. of consonants=",consonants)