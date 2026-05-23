arr=[2,4,5,8,1,10]
a=int(input("Enter the number to search: "))
i=0
if a in arr:
    while(arr[i]!=a):
        i+=1
    print(f"Number found at position {i+1}")

else:
    print("Number is not in array")