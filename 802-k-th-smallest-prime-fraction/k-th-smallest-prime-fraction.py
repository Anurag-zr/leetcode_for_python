class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                fraction = arr[i]/arr[j]
                heapq.heappush(heap,(fraction,(arr[i],arr[j])))

        
        for _ in range(k):
            a,b = heapq.heappop(heap)[1]

        return [a,b]