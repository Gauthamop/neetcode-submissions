class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #longest turbulent subarray
        longestlength=1  
        left=0 #left starts from 0
        n=len(arr)  #length of array
        right=1
        prev=""
        while right<n:
            if arr[right-1]>arr[right] and prev!=">":
                longestlength=max(longestlength,right-left+1)
                right+=1
                prev=">"
            elif arr[right-1]<arr[right] and prev!="<":  #if they are the same
                longestlength=max(longestlength,right-left+1)
                right+=1
                prev="<"

            else:
                right=right+1 if arr[right]==arr[right-1] else right
                left=right-1
                prev=""


        return longestlength

            




        