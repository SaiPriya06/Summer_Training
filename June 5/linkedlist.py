class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            
        np.next=temp.next
        temp.next=np
    
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None #last but before node
        
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(0,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def search(self,num):
        flag=0
        temp=self.head
        while temp!=None:
            if temp.data==num:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("yes,found")
        else:
            print("not found")
        
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
                
    def mid(self):
        if self.head is None:
            return None
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print(slow_ptr.data)
        
    def mid1(self):
        t=self.head
        c=0
        while t:
            c=c+1
            t=t.next
        c=c//2
        t=self.head
        for i in range(c):
            t=t.next
        print(t.data)
    
    def length(self):
        t=self.head
        c=0
        while t:
            c=c+1
            t=t.next
        if(c%2==0):
            print("even")
        else:
            print("odd")
    
    def length1(self):
        if self.head is None:
            return None
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr.next==None:
            print("odd")
        else:
            print("even")
            
    def sub(self):
        t=self.head
        c=1
        l=1
        while t.next:
            if (t.data==t.next.data -1):
                l=l+1
            else:
                c=max(c,l)
                l=1
            t=t.next
        c=max(c,l)
        print(c)
                            
obj=SLL()
#node creation_initialising
n=Node(10555)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1 #next node value
n2=Node(21)
n1.next=n2
n3=Node(22)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("before inserting 100")
obj.display()
print(" ")
print("after inserting 100 at begin")
obj.insert_beginning(100)
obj.display() #traverse
print(" ")
print("after inserting 555 at begin")
obj.insert_beginning(555)
obj.display()
print(" ")
print("after inserting 90 at end")
obj.insert_end(90)
obj.display()
print(" ")
print("after inserting 70 at pos 3")
obj.insert_pos(3,70)
obj.display()
print(" ")
print("after deleting at begin")
obj.delete_begin()
obj.display()
print(" ")
print("after deleting at end")
obj.delete_end()
obj.display()
print(" ")
print("after deleting at pos")
obj.delete_pos(2)
obj.display()
print(" ")
num=int(input("enter number"))
obj.search(num)
obj.mid()
obj.mid1()
obj.length()
obj.length1()
obj.sub()


