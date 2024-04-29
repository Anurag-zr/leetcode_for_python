class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # using recursion method
        # if(numRows == 0 ): return [[]]
        # if(numRows ==1 ): return [[1]]

        # prevRows = self.generate(numRows-1)
        # curRow = [1]*numRows

        # for i in range(1,numRows-1):
        #     curRow[i] = prevRows[-1][i-1] + prevRows[-1][i]

        # prevRows.append(curRow)
        # return prevRows
        

        # using combinatorial formula

        if numRows == 0 : return [[]]
        if numRows ==1 : return [[1]]

        ans = []
        ans.append([1])
        for i in range (1,numRows): 
            prevRow = ans[-1]
            curRow = [1]*(i+1)

            for j in range(1,i):
                curRow[j] = prevRow[j-1] + prevRow[j]

            ans.append(curRow)

        return ans

        return ans