class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number =[ '0','1','2','3','4','5','6','7','8','9'] 
        sign = ['-','+']
        
        N = ""
        
        for i in str:
            if i in sign or i in number:
                N = N+i
                sign = ""    # we only want to use the sign once 
            elif i ==' ' and len(N)==0:
                pass
            else:
                break
        if N=="" or N == "+" or N =="-":
            return 0
        N = int(N)
        big = 2**31
        Max = big -1
        Min = -1*big
        
        
        if N >  Max:
            return Max
        elif N < Min:
            return Min
        else: 
            return N 

if __name__ == '__main__':
    Solution = Solution()
    print Solution.myAtoi(" +435435 jfldsjflsdflksdjfj")