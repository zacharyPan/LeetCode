
# this solution passed 315/318 test. I think the logic is correct just not efficiency 


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Length= len(nums)

        if Length < 3:
            return []
        List = []
        listOfSet = []
        for i in range(0,Length-2):
            for j in range(i+1, Length-1):
                for k in range(j+1, Length):
                    numsI = nums[i]
                    numsJ = nums[j]
                    numsK = nums[k]
                    tempSet = {numsI, numsJ, numsK}
                    if (numsI+numsJ+ numsK == 0  ) and tempSet not in listOfSet:
                        List.append([numsI, numsJ, numsK])  
                        listOfSet.append(tempSet)

        return List