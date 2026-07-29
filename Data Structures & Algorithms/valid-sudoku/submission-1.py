from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(list)
        row = defaultdict(list)
        mat = defaultdict(list)
        for ind_r, rows in enumerate(board):
            for ind_c, val in enumerate(rows):
                if val == ".":
                    continue
                if val in row[ind_r]:
                    return False
                if val in col[ind_c]:
                    return False
                if val in mat[(ind_r // 3, ind_c // 3)]:
                    return False
                row[ind_r].append(val)
                col[ind_c].append(val)
                mat[(ind_r // 3, ind_c // 3)].append(val)
                
        return True
