s1=input("Enter text to check how many vowels is in the text: ")

vowels=list("aeiou")
count=0
consonants=0

for x in s1:
    if x in vowels:
        count+=1
    elif x==" " or x=="\t":
        pass
    else:
        consonants+=1

print(f"this text have\n    vowels: {count}\n    consonants: {consonants}  ")