class Solution(object):
    
    def minLength(self,strs):
        minLen = len(strs[0])
        for i in range(1,len(strs)):
            foo = len(strs[i])
            if foo < minLen:
                minLen = foo
        return minLen
               
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 :
            return "" 
        commonPrefix = ""
        minLen = self.minLength(strs)
        for j in range(0,minLen):
            for i in range(0,len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    return commonPrefix
            commonPrefix = commonPrefix + strs[0][j]
        return commonPrefix 

if __name__ == '__main__':
    print Solution().longestCommonPrefix(["abcdkjf","abcdklfjsd","abc"])