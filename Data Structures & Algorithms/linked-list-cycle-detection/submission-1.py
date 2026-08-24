# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #linked list cycle detection , #cycle means when any node is linked to a previous node , we can use a hashset to keep track of nodes we have already visited 
        #so we need a index value aswell, but that is not provided to us
        #can only be solved using linked list approach 
        hashset=set() #we can keep track of visited nodes

        curr=head #the starting value


        while (curr!=None):
    
            if curr not in hashset:
                hashset.add(curr)  #this adds the node itself
                curr=curr.next

            elif curr in hashset:
                return True

        
        return False

            


