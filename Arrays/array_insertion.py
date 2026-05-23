arr=[2,4,5,8,1,10]
a=int(input("Enter the position where you want to insert: "))-1
b=int(input("Enter a number to insert: "))
arr.insert(a,b)
for item in arr:
    print(item)