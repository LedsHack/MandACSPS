class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    return new_head

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


head = list_to_linked_list([1, 2, 3, 4])
new_head = swap_pairs(head)
print(linked_list_to_list(new_head))

head = list_to_linked_list([])
new_head = swap_pairs(head)
print(linked_list_to_list(new_head))

head = list_to_linked_list([1])
new_head = swap_pairs(head)
print(linked_list_to_list(new_head))