# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #singly linked list #can only move in one direction

        #storing the nodes in an array for access 

        nodes=[]
        cur=head
        while(cur!=None):
            nodes.append(cur)
            cur=cur.next


        #now we initilize two pointers
        index=len(nodes)-n  #this stops at the index of removal  #array method
        #next next exists

        #these nodes are already connected

        if index==0:
            return head.next

        nodes[index-1].next=nodes[index].next   

        return head        
    



        

