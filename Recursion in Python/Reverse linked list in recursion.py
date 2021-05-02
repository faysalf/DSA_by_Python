def reverseUtil(self, curr, prev):
    # If last node mark it head
    if curr.next is None:
        self.head = curr

        # Update next to prev node
        curr.next = prev
        return

    # Save curr.next node for recursive call
    next = curr.next

    # And update next
    curr.next = prev

    self.reverseUtil(next, curr)


# This function mainly calls reverseUtil()
# with previous as None

def reverse(self):
    if self.head is None:
        return
    self.reverseUtil(self.head, None)