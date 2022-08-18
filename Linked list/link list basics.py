class Node:

    def __init__(self, data):
        self.val = data
        self.next = None



#
class Linkedlist:

    def __init__(self):
        self.head = None


    def Append(self, new_data):

        current_node = Node(new_data)  # 100

        if self.head is None:
            self.head = current_node
            return

        temp = self.head.next
        while temp is not None:

            temp = temp.next

        temp = current_node


    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next


if __name__ == '__main__':
    l = Linkedlist()
    l.head = Node(1)
    l.head.next = Node(5)
    l.head.next.next = Node(100)

    l.print_linkedlist()