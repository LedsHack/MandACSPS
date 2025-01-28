class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def partition(head, x):
    smaller_head = ListNode(0)
    greater_head = ListNode(0)
    smaller = smaller_head
    greater = greater_head
    current = head

    while current:
        if current.val < x:
            smaller.next = current
            smaller = smaller.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    greater.next = None
    smaller.next = greater_head.next
    return smaller_head.next
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
head1 = createList([1, 4, 3, 2, 5, 2])
x1 = 3
result1 = partition(head1, x1)
printList(result1)

head2 = createList([2, 1])
x2 = 2
result2 = partition(head2, x2)
printList(result2)
