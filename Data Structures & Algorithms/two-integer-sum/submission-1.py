class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {n: i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            remainder = target-n
            # the current number we are comparing
            if remainder in indices and indices[remainder]!= i:
                return[i,indices[remainder]]
            
                

                