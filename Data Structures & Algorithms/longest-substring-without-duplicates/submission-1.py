class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #contiguous and not empty 
        #need to check if the substring is valid at all times (sliding window)
        hashset=set() #to keep track of duplicates
        #length of sliding window (right-left)+1

        left=0
        longest=0 #so far the longest length =0
        n=len(s)

        for right in range(n):
            while s[right] in hashset:  #its invalid, while the right element is still in the set , remove the current left and increase left                       #if this is going to remove stuff , its moving L and R to the right anways so it will be O(n)

                hashset.remove(s[left])
                left+=1

            w=(right-left)+1
            longest=max(longest,w)
            hashset.add(s[right])

        
        return longest


