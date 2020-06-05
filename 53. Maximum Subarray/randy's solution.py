class Solution:
    def maxSubArray(self, nums) -> int:
        local_sum = 0
        max_sum = -9223372036854775807
        
        for num in nums:
            local_sum += num
            if max_sum < local_sum:
                max_sum = local_sum

            if local_sum < 0:
                local_sum = 0

        return max_sum                
