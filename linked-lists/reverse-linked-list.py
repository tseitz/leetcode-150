from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


if __name__ == "__main__":
    # head = [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    assert Solution().reverseList(head) == [5,4,3,2,1]

    head = [1,2]
    assert Solution().reverseList(head) == [2,1]

    head = []
    assert Solution().reverseList(head) == []
