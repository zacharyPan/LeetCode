# my solution passed 2071 / 2085 test cases. although the algorithms and 
# logic is correct. it is O(m!) or O(n!) instead of O(m+n). However, 
# I spend a lot of time on it, so I don't want to discard all hard work 


# I submit again, and this time. totally passed!


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums2) > len(nums1):
            pass
        else:
            foo = nums2
            nums2 = nums1
            nums1 = foo
            
        a = len(nums1)
        b = len(nums2)
        median = (a+b)/2 
        total = a+b
        k = 0 
        for i in range(0, a ):
            if k > median:
                break 
     
            for j in range(k,len(nums2)):  
              
                if nums1[i] == nums2[j]:
                    nums2.insert(j, nums1[i])
                    k = k+1
                    break 
                elif nums1[i] < nums2[j]: 
                    nums2.insert(j, nums1[i])
                    k = k+1
                    break    
                elif j == len(nums2)-1 and nums1[i] > nums2[j]: 
                    nums2.append(nums1[i])
                    k = k +1
                    break 
                else: 
                    pass
                k = k+1
                

   
        goo = nums2[median]
        hoo = nums2[median-1]
                    
        if total % 2 == 1:
            return float(goo)
        else:
            return float(goo+hoo)/float(2)
            
if __name__ == '__main__':

    
    print Solution().findMedianSortedArrays([4,5,6],[1,2,3,19])    
            