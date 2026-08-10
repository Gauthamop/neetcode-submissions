class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #a boat can carry at most of two people at the same time
        #provided that the sum==limit
        #return the minimum number of boats to carry every given person 
        #all the people in the list must get on the boat 

        #we need to use two pointers aswell , all the people need to be accounted fo
        left=0 #start of the array
        right=len(people)-1 #at the end of the array

        boatcount=0
        people.sort() #o(nlogn)
        while left<=right: #should not cross, nor be equal to each other
            if  people[left]==limit:
                boatcount+=1
                left+=1
            elif people[right]==limit:
                boatcount+=1
                right-=1

            elif people[left]+people[right]>limit:
                right-=1
                boatcount+=1

            elif people[left]+people[right]<=limit:
                left+=1
                right-=1
                boatcount+=1
            

        return boatcount

        




        






        