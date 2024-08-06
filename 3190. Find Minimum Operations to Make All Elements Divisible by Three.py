# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/


def minimumOperations(nums: list[int]) -> int:
    operations = 0
    for num in nums:
        if num % 3 != 0:
            operations += 1
    return operations


# Example 1:
# Input:
nums = [1, 2, 3, 4]
print(minimumOperations(nums))
# Output: 3
# Explanation:
# All array elements can be made divisible by 3 using 3 operations:
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
