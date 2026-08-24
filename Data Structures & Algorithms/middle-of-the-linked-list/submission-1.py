# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #you are given the head of a singly linked list , return the middle node of the linked list

        curr=head  #currently at head
        #okay index is not provided here
        index=0
        while (curr!=None):
            curr=curr.next
            index+=1   #this gives us the length of the linked list
        #when index==0 then we have reached the index
        curr=head
        index=index//2
        while (curr!=None and index>0):
            curr=curr.next
            index-=1

        if curr and index==0:  #we have reached our destination
            return curr


    




        