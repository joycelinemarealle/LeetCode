# Last updated: 4/10/2025, 6:36:27 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #FIRST METHOD if can use built in
         newString = ""  #empty string
        #Loop through string copy alpha numeric to new string. make sure in lowercase
         for c in s:
            if c.isalnum(): 
                newString += c.lower()
         return newString == newString[::-1] #returns true if forward == reverse

