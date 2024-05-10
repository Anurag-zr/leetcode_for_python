class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # brute force
        # heap = []

        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         fraction = arr[i]/arr[j]
        #         heapq.heappush(heap,(fraction,(arr[i],arr[j])))

        
        # for _ in range(k):
        #     a,b = heapq.heappop(heap)[1]

        # return [a,b]

        # optimized T.C

        minHeap =[]

        for i in range(len(arr)-1):
            fraction = arr[i]/arr[-1]
            heapq.heappush(minHeap,(fraction,(i,len(arr)-1)))
        
        for _ in range(k-1):
            numInd,demInd = heapq.heappop(minHeap)[1]

            if(demInd-1>numInd):
                fraction = arr[numInd]/arr[demInd-1]
                heapq.heappush(minHeap,(fraction,(numInd,demInd-1)))
        

        numInd,demInd = heapq.heappop(minHeap)[1]
        return [arr[numInd],arr[demInd]]