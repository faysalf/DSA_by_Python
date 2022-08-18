class Node:

    def __init__(self, data):
        self.val = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)



a.next = b
print(a.next.val)



'''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node

list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3'''