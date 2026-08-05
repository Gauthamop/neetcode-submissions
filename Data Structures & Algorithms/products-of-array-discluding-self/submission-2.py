class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsum=[]  #stores the prefixproduct of all values before it
        for i,n in enumerate(nums):
            product=1 #this gives u the index value and the numberitself
            for j,k in enumerate(nums):
                if i==j:
                    continue
                product*=nums[j]
            productsum.append(product)


        return productsum



                



        