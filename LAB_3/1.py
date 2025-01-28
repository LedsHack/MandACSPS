class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return dummy.next

# Приклад 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
result = mergeTwoLists(list1, list2)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")

# Приклад 2
list1 = None
list2 = None
result = mergeTwoLists(list1, list2)
if result:
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
else:
    print("None")

# Приклад 3
list1 = None
list2 = ListNode(0)
result = mergeTwoLists(list1, list2)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
