# Last updated: 4/8/2025, 7:37:30 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Create set to hold values
        numSet = set(nums)
        longest = 0

        #Loop through nums and check starting of sequence
        for n in numSet:
            #check if number is begining of sequence(no left value) and in set
             if (n-1) not in numSet:
                length = 0
                while(n+length) in numSet: #just first number
                    length +=1 #keep on increasing to check consecutive number
                longest = max(longest, length)
        return longest
        



