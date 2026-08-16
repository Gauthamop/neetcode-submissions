class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        left=0
        count=[0]*26 # for all the characters in the alphabet
        n=len(s)
        for right in range(n):
            count[ord(s[right])-ord('A')]+=1
            while (right-left+1)-max(count)>k: #that means there are more characters than k to convert inorder for this to be a valid substring
                count[ord(s[left])-ord('A')]-=1 #we decrease the frequency
                left+=1

            longest=max(longest,(right-left+1))  #if valid

        return longest

