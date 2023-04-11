# Constraints:

# 2 <= nums.length <=104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists

# Question

#  Test Inputs

# nums = []

# Psuedocode Solution

# make a function called twoSum and pass in variables nums
# that have a list
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
# make an object
        d ={}
# loop over values and indices of list of nums
        for i, j in enumerate(nums):
# Check if target - value is in remainder
# if in remainder, return remainder list
# if not, add index to remainder

#Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []