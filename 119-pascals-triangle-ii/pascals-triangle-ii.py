class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

    # using combinatorial factor
    
        if (rowIndex == 0): return [1]

        prevRow =[1]
        curRow = [1]
        for i in range (1,rowIndex+1):
            curRow= [1]*(i+1)
            for j in range (1,i):
                curRow[j] = prevRow[j-1]+prevRow[j]

            prevRow = curRow
        return curRow
