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

def AddTwoList(head1,head2):
  if head1 is None or head2 is None:
    return
  new_head1=reverseLinkedList(head1)
  new_head2=reverseLinkedList(head2)
  fake_head=ListNode(None)
  current_node=fake_head
  temp_sum=0
  carry=0
  while new_head1 and new_head2:
    temp_sum=new_head1.value+new_head2.value+carry
    current_node.next=ListNode(temp_sum%10)
    carry=temp_sum//10
    current_node=current_node.next
    new_head1=new_head1.next
    new_head2=new_head2.next
  while new_head1:
    temp_sum=new_head1.value+carry
    carry=temp_sum//10
    current_node.next=ListNode(temp_sum%10)
    current_node=current_node.next
    new_head1=new_head1.next
  while new_head2:
    temp_sum=new_head2.value+carry
    carry=temp_sum//10
    current_node.next=ListNode(temp_sum%10)
    current_node=current_node.next
    new_head2=new_head2.next
  if carry>0:
    current_node.next=ListNode(carry)
  return reverseLinkedList(fake_head.next)


node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node7=ListNode(7)
node8=ListNode(8)
node1.next=node2
node2.next=node3

node7.next=node8
new_headhhhhh=AddTwoList(node1,node7)
print_LinkedList(new_headhhhhh)