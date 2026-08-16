class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #two integers k and threshold , return the number of subarrays of size (k) our window 
        #whose average is greater than or equal to threshold

        left=0
        n=len(arr)
        count=0 #current count is 0 of subarrays whose average is greater than or equal to threshold
        sum=0
        curr_avg=0
        #to grow our window
        for right in range(k):
            sum+=arr[right]    #takes the sum of the first k elements(starting window)


        curr_avg=sum/float(k)   #the first curr_avg
        if curr_avg>=threshold:
            count+=1

        curr_avg=0
        #for the numbers after the first k
        for right in range(k,n):
            sum+=arr[right]  #adding the next element to sum
            sum-=arr[right-k] #removing the element exiting the array from the sum

            curr_avg=sum/float(k)
            if curr_avg>=threshold:
                count+=1

        return count
            



        