# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class listNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None #prev is behind the cur        
        cur=head  #curr is at the start

        while (cur!=None):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        
        return prev


        
        
        


    

        