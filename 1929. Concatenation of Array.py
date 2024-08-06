# https://leetcode.com/problems/concatenation-of-array/

# method 1

def getConcatenation(nums: list[int]) -> list[int]:
    for i in  range(len(nums)):
        nums.append(nums[i])
    return nums

# Input
nums = [1, 2, 1]
print(getConcatenation(nums))
# Output: [1,2,1,1,2,1]

# Method 2

def getConcatenation(nums: list[int]) -> list[int]:
    return nums+nums

# Input
nums = [1, 2, 1]
print(getConcatenation(nums))
# Output: [1,2,1,1,2,1]
