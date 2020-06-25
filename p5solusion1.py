# I think this solution is logically correct. it only pass 41/103 case
# so I am looking for a better solution


class Solution(object):
    
    def palindromicCheck(self, s):
        print s, len(s)/2
        for i in range(0, len(s)/2):
            print s[i], s[-1-i]
            if s[i] != s[-1-i]:          
                return False
        return True
        
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s =="":
            return ""
        sList = list(s)
        MaxS = sList[0]
        for i in range(0,len(sList)):
            for j in range(i,len(sList)+1):
                if self.palindromicCheck(s[i:j]) and len(s[i:j])> len(MaxS):
                    MaxS = s[i:j]
        return MaxS
                    
                