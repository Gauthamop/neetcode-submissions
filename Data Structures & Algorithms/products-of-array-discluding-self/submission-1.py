class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        productarray=[]

        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i==j:
                    continue
                product*=nums[j]

            productarray.append(product)
        
        return productarray


