# https://leetcode.com/problems/number-of-good-pairs


def numIdenticalPairs(nums: list[int]) -> int:
    identicalPairs = 0

    for num1 in range(len(nums)):
        for num2 in range(num1 + 1, len(nums)):
            if nums[num1] == nums[num2] and num1 < num2:
                identicalPairs += 1
    return identicalPairs


# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input:
nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input:
nums = [1, 1, 1, 1]
print(numIdenticalPairs(nums))
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input:
nums = [1, 2, 3]
print(numIdenticalPairs(nums))
# Output: 0
