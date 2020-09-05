class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def print_LinkedList(cur):
    while cur:
        print(cur.value)
        cur = cur.next



def reverseLinkedList(head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node



def findTheMedium(head):
    if head is None:
        return
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def palidrom(head):
    if head is None:
        return -1
    fake_head = ListNode(None)
    fake_head.next = head
    Prev_mid = findTheMedium(fake_head)
    Mid_After = Prev_mid.next
    Prev_mid.next = None
    head1 = head
    head2 = reverseLinkedList(Mid_After)
    while head1 and head2:
        if head1.value != head2.value:
            return False
        else:
            head1 = head1.next
            head2 = head2.next
    return True


node1 = ListNode('a')
node2 = ListNode('b')
node3 = ListNode('c')
node4 = ListNode('d')
node5 = ListNode('c')
node6 = ListNode('b')
node7 = ListNode('a')
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

palidromLinkedlist = palidrom(node1)
print(palidromLinkedlist)


