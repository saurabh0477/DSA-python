arr=[2,4,5,8,1,10]
b=int(input("Enter a number to delete: "))

if b in arr:
    for item in arr:
        if item==b:
            arr.remove(b)
            print("number deleted successfully")
else:
    print(f"{b} is not in array")
    
for item in arr:
    print(item)