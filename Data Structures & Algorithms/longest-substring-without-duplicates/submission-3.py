class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #here we need to find the longest substring without repeating characters
        n=len(s)
        left=0
        longlength=0  #the current  longest length #minimum is 1
        #to maintain and check for duplicate copies we create an hashset
        hashset=set() #if an element is already in the hashset , we remove the left element , and move the left pointer to the right, if the right element is not there , just add to hashset and proceed 


        for right in range(n):
            while s[right] in hashset:   #if the right element is in the hashset
                    hashset.remove(s[left])
                    left+=1

            window=(right-left)+1
            longlength=max(longlength,window)
            hashset.add(s[right])
                


        return longlength


        