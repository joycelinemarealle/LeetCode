# Last updated: 4/1/2025, 8:05:23 PM
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Hash map key is col number value a set of all numbers col. Set distinct numbers
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) #key (r//3,c//3)

        #Iterate through entire grid
        for r in range (9):
            for c in range (9):
                #if position empty skips
                if board[r][c] == ".":
                    continue
                    #Check for duplicates if current in current row --> row hash map 
                    #r contains a set of @ row with all its elemet
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[r//3,c//3]):
                 return False
                #if not duplicate then add to dict
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c]) #eg value 5 at 0,0 board[0,0]
        return True
            





        