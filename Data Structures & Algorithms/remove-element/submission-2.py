class Solution:
    # remove all `val` from `nums`
    def removeElement(self, nums: List[int], val: int) -> int:
        array_size: int = len(nums);
        
        index: int = 0;
        while index < array_size:
            if val == nums[index]:
                nums[index] = nums[array_size-1];
                array_size -=1
            else:
                index +=1
        return array_size;