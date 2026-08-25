"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #copy a list with random pointers attached 
        old_to_copy={}  #created an hashmap to keep track of used nodes , old and its copy 


        curr=head #current head of the linked list

        while(curr!=None): #1st pass , make copies of the node and store their copy aswell in an hashmap 
            #need to create a nodecopy
            copy=Node(curr.val)   #creates a node and stores it in copy
            old_to_copy[curr]=copy   #old_to_copy

            curr=curr.next

        
        #2nd pass , through the hashmap for every node we send it to the next node value and then we randomize random values 

        curr=head #reset current pointer
        while(curr!=None):
            copy=old_to_copy[curr]
            copy.next=old_to_copy.get(curr.next)
            copy.random=old_to_copy.get(curr.random)

            curr=curr.next



        return old_to_copy.get(head)

        

        