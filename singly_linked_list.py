class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LL:
    def __init__(self):
        self.head=None

    def print_(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.next
        print()
        print(" head is" ,self.head.data)

    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


    def add_end(self,data):
        new_node=Node(data)
        n=self.head
        if self.head is None:
            self.head= new_node
        while n.next   is not None:
            n=n.next
        n.next=new_node


    def add_after(self,data,x):
        n=self.head
        while n.next is not None:
            if n.data==x:
                break
            n=n.next

        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node

    def add_befor(self,data,x):
        if self.head.data==x:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        n=self.head
        while n.next is not None:
            if n.next.data==x:
                break
            n=n.next
        new_node=Node(data)
        new_node.next=n.next
        n.next=new_node

ll=LL()
ll.add_begin(10)
ll.add_begin(20)
ll.add_end(60)
ll.add_befor(50,60)
ll.add_befor(30,20)
ll.add_after(80,60)
ll.print_()