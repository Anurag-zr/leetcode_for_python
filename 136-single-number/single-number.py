class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map ={}
        for i in range (0,len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1;

        for key,value in map.items():
            if(value==1): return key

        return -1
