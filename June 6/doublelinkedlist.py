class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addback(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    
    def addfront(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    
    def display(self):
        t=self.head #temp=first node
        while t!=None:
            print(t.data,end="->")
            t=t.next
        print()
    
    def revdisplay(self):
        t=self.tail #temp=first node
        while t!=None:
            print(t.data,end="->")
            t=t.prev
        print()
        
    def search(self,x):
        h=self.head
        t=self.tail
        flag=0
        while h!=t and h!=t.next:
            if h.data==x or t.data==x:
               return "found"
            h=h.next
            t=t.prev
        if h.data==x:
            return"found"
        else:
            return "not found"
        
    def length(self):
        h=self.head
        t=self.tail
        while h!=t and t!=t.next:
            h=h.next
            t=t.prev
        if h==t:
            print("odd")
        else:
            print("even")
            
    def palindrome(self):
        h=self.head
        t=self.tail
        while h!=t and t!=t.next:
            if(h.data!=t.data):
                return "not palindrome"
            h=h.next
            t=t.prev
        return "palindrome"
    
'''3 5 7 8 9 10 12 15
9 10 12 15 3 5 7 8'''
    def halfsplit(self):
        f=self.head
        s=self.head
        while(f=None):
            f=f.next.next
            s=s.next
        s.tail.next=self.head
        s.head.prev=self.tail
        t1=s.prev
        t1.next=None
        s.prev=None
        s.head=s
        s.tail=t1
        
        
        
            

l=dll()
l.head=Node(5)
l.tail=l.head
l.addback(20)
l.addfront(30)
l.addback(50)
l.addback(60)
#l.addfront(80)
l.display()
print()
l.revdisplay()
print(l.search(20))
l.length()
print(l.palindrome())

        
        


        
        
            