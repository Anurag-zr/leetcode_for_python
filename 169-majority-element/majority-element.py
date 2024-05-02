class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        start =0
        end = len(nums)-1

        mid = start + (end -start)//2

        return nums[mid]
