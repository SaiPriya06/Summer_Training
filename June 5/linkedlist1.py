'''6 7 4 8 4 2 0 1
67 64 64 68 ......all possible pairs'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
         
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next#establishing link
    def pairs(self):
        t=self.head
        while t.next!=None:
            t1=t.next
            while t1!=None:
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
obj=SLL()
#node creation_initialising
n=Node(6)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(7)
n.next=n1 #next node value
n2=Node(4)
n1.next=n2
n3=Node(8)
n2.next=n3
n4=Node(4)
n3.next=n4
n5=Node(2)
n4.next=n5
n6=Node(0)
n5.next=n6 #next node value
n7=Node(1)
n6.next=n7
obj.display()
print()
obj.pairs()