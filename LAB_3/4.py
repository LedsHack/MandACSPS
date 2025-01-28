class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return head

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev, curr = None, second
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    return head
def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(head1)
printList(head1)

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorderList(head2)
printList(head2)
