class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #in a sudoku a number cannot repeat in the same row , column or in a subgrid , in this case in a 9*9 sudoku board , the same number cannot be present in a 3*3 subgrid, since we are dealing with a list of numbers , hashmap also needs to be in list
        hashmap_rows=defaultdict(list)
        hashmap_cols=defaultdict(list)
        hashmap_sub_grid=defaultdict(list)
        #created the hashmap , now we traverse through the board

        for i,rows in enumerate(board):
            for j,nums in enumerate(rows):
                if nums==".":
                    continue
                if nums in hashmap_rows[i] or nums in hashmap_cols[j] or nums in hashmap_sub_grid[(i//3,j//3)]:
                    return False

                hashmap_rows[i].append(nums)
                hashmap_cols[j].append(nums)
                hashmap_sub_grid[(i//3,j//3)].append(nums)
                
        return True