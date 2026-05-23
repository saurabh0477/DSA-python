a=input("Enter a text: ")
text=a.split()

ab=[]
for word in text:
    count_letter=0
    for letter in word:
        count_letter+=1
    ab.append(count_letter)
        

greatest=max(ab)
x=0
for i in ab:
    if i==greatest:
        print(text[x])
    x+=1

