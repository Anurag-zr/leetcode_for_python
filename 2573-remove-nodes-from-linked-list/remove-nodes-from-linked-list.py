# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
# stack approach
# time complexity: O(n) space complexity: O(n)
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack =[]
    #     cur = head

    #     while cur:
    #         while stack and stack[-1].val < cur.val :
    #             stack.pop()
    #         stack.append(cur)   
    #         cur = cur.next

    #     cur = None
    #     while stack:
    #         new = stack.pop()
    #         new.next = cur
    #         cur = new
        
    #     return cur

# recursive approach
# time complexity : O(n) space complexity : o(n)
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if(head == None):
    #         return None

    #     node = head
    #     nxtGreater = self.removeNodes(node.next)

    #     node.next = nxtGreater

    #     if( nxtGreater == None or node.val>=nxtGreater.val):
    #         return node

    #     return nxtGreater

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        prev, curr = None, head
        while curr:
            curr.next,prev,curr = prev,curr,curr.next


        # Initialize a dummy node to hold the result
        dummy_head = ListNode(-1)
        temp_prev, curr = dummy_head, prev
        # Traverse the reversed list, keeping nodes greater or equal to previous
        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = curr
                curr = curr.next
            else:
                curr = curr.next
        temp_prev.next = None
        
        # Reverse the result list again
        new_prev = None
        curr = dummy_head.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev        






