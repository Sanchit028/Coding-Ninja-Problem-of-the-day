class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert(head, n, pos, val):
    new_node = Node(val)

    if pos == 0:
        new_node.next = head
        return new_node

    current = head
    prev = None
    count = 0
    while current and count < pos:
        prev = current
        current = current.next
        count += 1
    
    prev.next = new_node
    new_node.next = current
    
    return head
