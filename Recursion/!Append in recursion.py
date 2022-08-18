# Function to insert a new node at the
# end of linked list using recursion.
def insertEnd(head, data):
    # If linked list is empty, create a
    # new node (Assuming newNode() allocates
    # a new node with given data)
    if (head == None):
        return newNode(data)

    # If we have not reached end,
    # keep traversing recursively.
    else:
        head.next = insertEnd(head.next, data)

    return head

# This code is contributed by divyeshrabadiya07