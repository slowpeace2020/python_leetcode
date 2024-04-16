class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pre_row = [poured]

        for i in range(1,query_row+1):
            cur_row = []
            for j in range(i+1):
                if j==0 or j==i:
                    value = max(0,pre_row[0]-1)/2
                else:
                    value = (max(0,pre_row[j-1]-1)+max(0,pre_row[j]-1))/2
                cur_row.append(value)
            pre_row = cur_row

        return min(1,pre_row[query_glass])