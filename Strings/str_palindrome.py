string=input("Enter a word to check it is palindrome: ")
rev=string[::-1]

#palindrome means string= reverse string
#eg. if we read madam backwards we still get madam

if string==rev:
    print(f"{string} is palindrome ")

else:
    print(f"{string} is not palindrome ")
