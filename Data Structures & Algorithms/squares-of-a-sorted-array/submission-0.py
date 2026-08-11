class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left=0
        right=len(nums)-1
        while left<=right:
            left_squared = nums[left]*nums[left]
            right_squared = nums[right]*nums[right]
            if (left_squared) < (right_squared):
                result.append(right_squared)
                right-=1
            else:
                result.append(left_squared)
                left+=1
        return result[::-1]