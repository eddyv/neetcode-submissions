class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        ans = [0] * (2*nums_size)
        ans[0:nums_size] = nums
        ans[nums_size:2*nums_size] = nums
        return ans