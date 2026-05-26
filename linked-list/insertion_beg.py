class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def insertBeg(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next




x=linkedList()
x.insertBeg(3)
x.insertBeg(10)
x.display()