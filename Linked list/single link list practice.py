class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        current_data = Node(new_data)
        if self.head is None:
            self.head = current_data
            return

        l = self.head.next
        while l is not None:
            l = l.next
        l = current_data

    def printlink(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

if __name__ == "__main__":
    f = linkedlist()
    f.head = Node(10)
    f.head.next = Node(20)
    f.head.next.next = Node(50)
    f.printlink()