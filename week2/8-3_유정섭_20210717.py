# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# CODE GOES HERE
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    answer = head
    prev = None
    curr = head
    while curr:
      next = curr.next
      answer = curr
      answer.next = prev
      prev = answer
      curr = next
    return answer

# TC
lnode = ListNode(1, ListNode(2, ListNode(3)))

# Print TC
curr = lnode
while curr:
  print(curr.val)
  curr = curr.next

rnode = Solution().reverseList(lnode)
curr = rnode
while curr:
  print(curr.val)
  curr = curr.next