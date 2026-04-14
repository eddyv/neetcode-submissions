class Solution:
    # remove all `val` from `nums`
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val);
        return len(nums);