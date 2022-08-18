def traverse(head):
    if (head == None):
        return

    # If head is not None, print current node
    # and recur for remaining list
    print(head.data, end=" ");
    traverse(head.next)

# This code is contributed by Pratham76