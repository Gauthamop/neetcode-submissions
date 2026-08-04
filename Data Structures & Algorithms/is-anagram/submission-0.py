class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        #adding elements into hashmap
        if len(s)!=len(t):
            return False
        
        s_list=[]
        t_list=[]
        for i in range(n):
            s_list.append(s[i])
            t_list.append(t[i])
        
        s_list.sort()
        t_list.sort()
        for i in range(n):
            if s_list[i]!=t_list[i]:
                return False

        return True










            
