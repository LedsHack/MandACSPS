class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Функція для виведення списку для перевірки результату
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = deleteDuplicates(head1)
printList(result1)

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = deleteDuplicates(head2)
printList(result2)
