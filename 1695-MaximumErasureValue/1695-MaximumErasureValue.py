class Solution(object):
    def maximumUniqueSubarray(self, nums):
        # Initialization
        window_start, sum_of_elements, max_score = 0, 0, 0
        num_freq = {}

        # Slide the window from window_start to window_end
        for window_end in range(len(nums)):
            right_num = nums[window_end]

            # Track the frequency of the current number
            if right_num not in num_freq:
                num_freq[right_num] = 1
            else:
                num_freq[right_num] += 1

            # Add the current number to the sum of the window
            sum_of_elements += right_num

            # Shrink the window if we have a duplicate
            while num_freq[right_num] > 1:
                left_num = nums[window_start]
                sum_of_elements -= left_num
                num_freq[left_num] -= 1
                if num_freq[left_num] == 0:
                    del num_freq[left_num]
                window_start += 1

            # Track the maximum score
            max_score = max(max_score, sum_of_elements)

        # Return the maximum sum
        return max_score