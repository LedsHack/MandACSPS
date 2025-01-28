import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
def mergeKLists(lists):
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, lists[i])
    head = ListNode()
    current = head
    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, node.next)
    return head.next

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

lists1 = [createList([1, 4, 5]), createList([1, 3, 4]), createList([2, 6])]
merged1 = mergeKLists(lists1)
printList(merged1)

lists2 = []
merged2 = mergeKLists(lists2)
printList(merged2)

lists3 = [createList([])]
merged3 = mergeKLists(lists3)
printList(merged3)
