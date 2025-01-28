class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def doubleNumber(head):
    carry = 0
    current = head
    while current:
        total = current.val * 2 + carry
        current.val = total % 10
        carry = total // 10
        if current.next is None and carry:
            current.next = ListNode(carry)
            carry = 0
        current = current.next
    return head

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

head1 = ListNode(1, ListNode(8, ListNode(9)))
doubled_head1 = doubleNumber(head1)
printList(doubled_head1)

head2 = ListNode(9, ListNode(9, ListNode(9)))
doubled_head2 = doubleNumber(head2)
printList(doubled_head2)
