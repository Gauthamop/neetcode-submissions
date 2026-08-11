class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #we need to return k ---> bananas-per-hour eating rate : basically how many banannas can koko eat in an hour
        #so every hour from a pile u can eat k bananas , if the pile has less than k bananas , u finish that pile and wait for the next hour , return k , such that u can eat all the bananas within h hours


        piles.sort() #sort the array first , we take the minimum pile amount as the base eating rate 

        left=1
        right=max(piles)
        res=right

        while left<=right:
            k=left+(right-left)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)

            if hours<=h:
                res=min(res,k)
                right=k-1
            else:
                left=k+1  #here k is the middle value


        return res





        