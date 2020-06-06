class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for num in nums:
            if num < target:
                i += 1
            else:
                return i
        else:
            return i
            