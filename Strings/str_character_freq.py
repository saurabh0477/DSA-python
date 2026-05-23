s1=input("Enter a text: ")
a=input("Enter a character to check the frequency in the text: ")


def freq():
    count=0
    for i in s1:
        if a==i:
            count+=1

    print(f"Frequency of {a}: {count}")

freq()