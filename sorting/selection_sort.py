l1=[7,5,8,4,2]

for st in range(len(l1)-1):
    small=st
    for i in range(st+1,len(l1)):

        if(l1[i]<l1[small]):
            small=i

    temp=l1[st]
    l1[st]=l1[small]
    l1[small]=temp


print(l1)
            

        