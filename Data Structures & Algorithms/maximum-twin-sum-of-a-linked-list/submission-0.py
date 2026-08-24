# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        #maximum twin sum of a linked list , size of the linked list is N(even)(0,1,2,3) index
        #i-th index of the linked list is known as the twin of the n-1-i node if 0<i<(n/2)-1

        #let me try with two pointers right now

        arr=[]
        curr=head
        while (curr!=None):
            arr.append(curr.val)
            curr=curr.next


        left=0 #first element
        right=len(arr)-1 #last element
        maxsum=0
        sum=0
        while left<=right: #can be equal but cannot cross
            sum=arr[left]+arr[right]
            maxsum=max(maxsum,sum)
            left+=1
            right-=1

        
        return maxsum

        