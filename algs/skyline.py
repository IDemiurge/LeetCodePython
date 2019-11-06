# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        vert=self.getSkyline(grid, True)
        hor=self.getSkyline(grid, False)
        # each cell can be increased up to the point when it becomes greatest in either hor or vertical skyline
        total=0
        for x in range (len(grid)):
            for y in range (len(grid[x])):
                val=grid[x][y]
                byY=vert[y]-val
                byX=hor[x]-val
                total+=min(byX, byY)
        return total
        
    def getSkyline(self, grid, hor):
        index=0
        skyline=[0]*len(grid[0])
        if (hor):
            for line in grid:
                maxi=0
                for i in line:
                    if (i>=maxi):
                        maxi=i
                        skyline[index]=maxi
                index+=1
        if not (hor):
            for x in range (len(grid)):
                maxi=0
                for line in grid:
                    i=line[x]
                    if (i>=maxi):
                        maxi=i
                        skyline[index]=maxi
                index+=1
        return skyline
