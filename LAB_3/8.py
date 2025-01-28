class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head, k):
    if not head or k == 1:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    def reverse_group(start, k):
        prev = None
        current = start
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    while True:
        group_start = prev_group_end.next
        group_end = prev_group_end
        for _ in range(k):
            group_end = group_end.next
            if not group_end:
                return dummy.next
        next_group_start = group_end.next
        group_end.next = None
        prev_group_end.next = reverse_group(group_start, k)

        group_start.next = next_group_start
        prev_group_end = group_start
    return dummy.next

def createList(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

head1 = createList([1, 2, 3, 4, 5])
k1 = 2
result1 = reverseKGroup(head1, k1)
printList(result1)

head2 = createList([1, 2, 3, 4, 5])
k2 = 3
result2 = reverseKGroup(head2, k2)
printList(result2)
