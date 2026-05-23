arr=[2,4,5,8,1,10]
a=int(input("Enter the number which you want to update: "))
b=int(input("Enter the new number: "))
x=0
if(a in arr):
    for i in arr:
        if i==a:
            arr[x]=b
            print("Updated successfully !")
        x+=1

else:
    print(f"{a} is not in array")
    
for item in arr:
    print(item)