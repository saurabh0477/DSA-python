#Anagram menas two words contain the same letters with the same frequency but i different order
#eg. evil -> live

word1=input("Enter first word: ")
word2=input("Enter second word: ")
word1_sort=sorted(word1)
word2_sort=sorted(word2)

if word1_sort==word2_sort:
    print("both words are anagram")

else:
    print("Not anagram !")


