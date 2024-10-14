class Solution(object):
    def lengthOfLongestSubstring(self, s):

        #1 Initialization
        window_start = 0
        max_length = 0
        char_freq = {}

        #2 Slide window
        for window_end in range (len(s)):
            #3Process each character of s and add to hashmap
            right_char = s[window_end]

            if right_char not in char_freq:
                char_freq[right_char] =1

            else:
                char_freq[right_char] +=1

            #4 Shrink window when frequency of char > 1
            while char_freq[right_char] > 1:
                left_char = s[window_start]
                
                #Rebalance hashmap
                char_freq[left_char] -=1
                if char_freq[left_char] == 0: #if after reducing by 1 becomes zero then remove
                    del char_freq[left_char]  
                #Move window ahead
                window_start +=1
            
            max_length = max (max_length, window_end-window_start+1)
        return max_length

        

      
        