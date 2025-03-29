# Last updated: 3/29/2025, 12:56:56 PM
# from collections import defaultdict
# from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res = {} # mapping charCount to list of anagrams
         res = defaultdict(list) #
        #Loop through array
         for s in strs:
            #empty array to hold char count. 26 empty sizne a-z has 26 char
            count = [0] *26
            #Iterate through every char  in string and keep track of count
            for c in s:
                count[ord(c) - ord('a')] +=1 #map a to index 0 and z to index 25
            #add key:value pair
            #res[count].append(s) #list cannot be key so convert to tuple
            res[tuple(count)].append(s) #tuple non mutable
            #issue if count does not exist so adjust to defaultdict
         return list(res.values())
