class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        a=-1
        b=-1
        for i in range(len(grid)):
            for j in range(len(grid)):
                res.append(grid[i][j])
        res.sort()
        for ele in res:
            if res.count(ele)>1:
                b=ele
        for i in range(1,len(res)+1):
            if i not in res:
                a=i
        return [b,a]
