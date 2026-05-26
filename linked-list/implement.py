class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        print(data)
       

x=node(4)
y=node(8)
print(x.next)

x.next=y
y.next=None