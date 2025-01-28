class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

head1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = head1.next
deleteNode(node_to_delete)
printList(head1)

head2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = head2.next.next
deleteNode(node_to_delete)
printList(head2)
