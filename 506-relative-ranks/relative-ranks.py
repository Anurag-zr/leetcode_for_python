class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score,reverse=True)
        #print(sortedScore)

        ans=[""]*len(score)
        position = 1
        for item in sortedScore:
            rank = str(position)
            if(rank == "1"):
                rank = "Gold Medal"
            if(rank == "2"):
                rank = "Silver Medal"
            if(rank == "3"):
                rank = "Bronze Medal"
            for i in range(0,len(score)):
                if(item == score[i]):
                    ans[i]=rank
                    position+=1
                    break
        return ans