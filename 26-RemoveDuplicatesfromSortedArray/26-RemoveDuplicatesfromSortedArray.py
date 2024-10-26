class Solution(object):
    def removeDuplicates(self, nums): 
        #initialization
        next_non_duplicate =1
        #pointer iterates through array
        i = 1
        while i < len(nums):
            #if previous element not same then next non duplicate is equal to value at iterator
            if nums[next_non_duplicate-1] != nums[i]:
                nums[next_non_duplicate] = nums[i]
                next_non_duplicate +=1 #move to next
            i+=1
        return next_non_duplicate

        """
        :type nums: List[int]
        :rtype: int
        """
        