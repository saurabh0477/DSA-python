l1=[3,5,8,4,2]
# l1=[1,2,3,4,5]
loop=len(l1)-1 #4

x=1
swapped=False

while(x<=loop):
    for i in range(0,loop):
        if l1[i]<=l1[i+1]:
            pass
        else:
            temp=l1[i]
            l1[i]=l1[i+1]
            l1[i+1]=temp
            swapped=True
            
    if(swapped==False):
        break
    loop-=1

print(l1)


