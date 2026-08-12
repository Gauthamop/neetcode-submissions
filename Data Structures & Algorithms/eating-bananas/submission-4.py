class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #we need to return k ---> bananas-per-hour eating rate : basically how many banannas can koko eat in an hour
        #so every hour from a pile u can eat k bananas , if the pile has less than k bananas , u finish that pile and wait for the next hour , return k , such that u can eat all the bananas within h hours


        piles.sort() #sort the array first , we take the minimum pile amount as the base eating rate 

        left=1  #binary searching using k as the pointers 
        right=max(piles)
        res=right

        while left<=right:
            k=left+(right-left)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)

            if hours<=h:  #here its taking less hours compared to h , meaning high k , but we need to minimize k 
                res=min(res,k)
                right=k-1
            else:
                left=k+1  #here k is the middle value , #its taking more hours with the current k to eat all the bannanas


        return res





        