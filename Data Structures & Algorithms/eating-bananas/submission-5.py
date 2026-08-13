class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() #first we sort the pile so that we can apply binary search to it
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
                left=k+1


        return res

        