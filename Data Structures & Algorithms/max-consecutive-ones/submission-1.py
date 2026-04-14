class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones: int = 0;
        current_consecutive_ones: int = 0;
        for num in nums:
            if num == 1:
                current_consecutive_ones+=1;
            else:
                current_consecutive_ones = 0;
            if current_consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = current_consecutive_ones;
        return max_consecutive_ones;

        