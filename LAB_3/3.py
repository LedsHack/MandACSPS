class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def hasCycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
def printResult(head):
    if hasCycle(head):
        print("Цигл знайдено")
    else:
        print("Без циклу")


head1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
head1.next.next.next.next = head1.next
printResult(head1)

head2 = ListNode(1, ListNode(2))
head2.next.next = head2
printResult(head2)

head3 = ListNode(1)
printResult(head3)
