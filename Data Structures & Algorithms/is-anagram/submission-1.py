class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #coming to valid anagram , valid anagram states that two words need to consist of the same number of letter's each , so here we need to keep track of the letter + its frequency in the particular word
        #we can try hashmap 

        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int) #created an hashmap which will keep track of the letter and its count
        if len(s)!=len(t):   #base condition
            return False
        for i in range(len(s)):
            hashmap1[ord(s[i])-ord('a')]+=1  #increase the count
            hashmap2[ord(t[i])-ord('a')]+=1
        
        return hashmap1==hashmap2



            
        