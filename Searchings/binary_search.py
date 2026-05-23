# binary searching is a searching algorithm that works on sorted array.
#instead of checking one-by-one, it checks the middle element and divides the array into halves 

arr=[10,20,30,40,50,60,70]
target=60

st=0
end=len(arr)-1

while(st<=end):
    half=(st+end)//2

    if(arr[half]==target):
        print(f"{target} found at index {half}")
        break

    elif(arr[half]<target):
        st=half+1

    else:
        end=half-1



    

# time complexity of binary search:
#     Best case= O(1)
#     worst case= O(log n)