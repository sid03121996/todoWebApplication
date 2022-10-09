class Node():

    def __init__(self,value,next=None):
        self.next=next
        self.value=value

class LinkedList:

    def __init__(self):
        self.head=None



def is_circular(head):

    slow=head
    fast=head

    while fast != None:
        slow = slow.next

        if fast.next != None:
            fast= fast.next.next

        else:
            return f'Given Linked List is not Circular'

        if slow is fast:
            return f'Given Linked List is Circular'

    return f'Given Linked List is not Circular'


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

node = LinkedList()

node.head = first
node.head.next = second
second.next = third
third.next = second

print(is_circular(node.head))
