class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given an array of bananas(in ith pile ) h--> is the total number of hours we have to eat all the bananas, at each pile u can eat the bananas only for an hour , if u finish eating based on ur eating rate 
        #u cant move onto the next pile untill the next hour
        #we can use binary search to go through the array both sides , chose K , based on k calculate 

        piles.sort() # we sort the array before hand
        left=1
        right=max(piles)
        res=right #as of right now result will store the max(eating rate)
        while left<=right:
            k=left+(right-left)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:  #this means that koko is eating the bananas way to fast 
                res=min(res,k)
                right=k-1

            else:  #this means koko is eating the bananas way too slow
                left=k+1


        return res






    

        