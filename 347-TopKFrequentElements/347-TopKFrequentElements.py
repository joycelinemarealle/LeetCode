# Last updated: 3/31/2025, 6:47:04 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Bucket sort algorithm grouping numbers based on frequency
        count = {} #key to value num:count
        freq = [[] for i in range(len(nums)+1)] #[[]...[]] emptylist that contains len(nums)+1 lists

        #Add count of each element in the map
        for n in nums:
            count[n] = 1+ count.get(n,0)
        
        #Add in freq array the numbers in each frequency rep by index
        #Iterate through the dictionary
        for n,c in count.items(): #key:value pair
            freq[c].append(n)

        #in freq array return last 2k
        res = []
        for i in range(len(freq)-1,0,-1):#Start from last index
            #iterate through list in freq array
            for n in freq[i]: #could be empty of have number, or multiple in a list
                res.append(n)
                if len(res) == k: #stop appending once k reached
                    return res




        #Track count of each element
        #Add list of numbers in array where each index reps the frequency. Size limited to len (input)
        #Pop the last K elements of array and add to new array
             # if result array == k return result array
 
 
 
 