# Last updated: 3/29/2025, 10:24:24 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #empty hash map
        countS, countT = {}, {}

        #check if length same
        if len(s) != len(t):
            return False #cannot be an anagram
        
        #Add the char + counts in map
        #Loop through len of one of the string since have same length
        for i in range (len(s)): #we see a char and increment by1
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            #if char not exist then default 0 instead of error from 1+ countS[s[i]]
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        #loop through all keys in hash map and check the counts
        for c in countS:
            if countS[c] != countT.get(c,0): 
                return False

        return True #anagram



#clarfying qns about input. Does lower or upper case matter? Does special character matter, space, ', etc
#anagram input same char +len different order
#STEPS thought process
#check if len of two strings the same first. if not return false
#Loop length of s to  to create  2 hash maps that store t char + the count of char  s + t
#Iterate through each key  of s and check if the counts match ,
    #if not return false t
# If all match then reuren true

#memory O(s+t). store char in 2 hashmap
#time O(s+t) loop through each string to put in hashmap