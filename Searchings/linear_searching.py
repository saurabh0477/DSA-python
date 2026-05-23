# linear searching means checking elements one-by-one until target is found

arr=[10,20,30,40,50,60,70]
target=60
index=-1

for i in arr:
    index+=1
    if i==target:
        print(f"{target} found at index {index}")

# time complexity of linear search:
#     Best case= O(1)
#     worst case= O(n)