class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #permutation in string
        #we can create 2 hashtables
        counts1=[0]*26
        counts2=[0]*26
        n1=len(s1)
        n2=len(s2)
        for char in range(n1):                    #we added it to our count
            counts1[ord(s1[char])-ord('a')]+=1

        #fixed length sliding window can be implemented here
        if n1>n2:
            return False

        for right in range(n1): #we going based on n1(current window length)
            counts2[ord(s2[right])-ord('a')]+=1 #so add all the elements in that window

        if counts1==counts2:
            return True
    
        
        #now for outside the window
        for right in range(n1,n2):
            counts2[ord(s2[right])-ord('a')]+=1
            counts2[ord(s2[right-n1])-ord('a')]-=1

            if counts2==counts1:
                return True

        
        return False



        






        