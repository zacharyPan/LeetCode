class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        newRow = ""
        gap1 = (numRows-1)*2
        gap2 = 0 
        for i in range(0,numRows):
            position = i
            k = 1
            while position < len(s):     
                
                if k%2 == 1 and gap1 != 0:
                    newRow = newRow + s[position]
                    position = position + gap1
                elif k%2 == 0 and gap2 !=0 :
                    newRow = newRow + s[position]
                    position = position + gap2
                else:
                    pass
                k = k+1
                
            gap1 = gap1-2
            gap2 = gap2+2

        return newRow

if __name__ == '__main__':

    
    print Solution().convert("dlkfjdlsjfldsjfldsjkfldsjkflkdsj",3)