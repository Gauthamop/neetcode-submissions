class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_rows=defaultdict(list)
        hashmap_cols=defaultdict(list)
        hashmap_subgrid=defaultdict(list)
        #hashmaps created 


        for i,rows in enumerate(board):
            for j,nums in enumerate(rows):
                if nums==".":
                    continue
                if nums in hashmap_rows[i] or nums in hashmap_cols[j] or nums in hashmap_subgrid[(i//3,j//3)]:
                    return False

                hashmap_rows[i].append(nums)
                hashmap_cols[j].append(nums)
                hashmap_subgrid[(i//3,j//3)].append(nums)

        return True


        