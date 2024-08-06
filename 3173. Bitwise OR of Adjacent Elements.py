# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/


def orArray(nums: list[int]) -> list[int]:
    answer = []
    for i in range(0, len(nums) - 1):
        answer.append(nums[i] | nums[i + 1])
    return answer


# Example 1:
# Input:
nums = [1, 3, 7, 15]
print(orArray(nums))
# Output: [3,7,15]

# Example 2:
# Input:
nums = [8, 4, 2]
print(orArray(nums))
# Output: [12,6]

# Example 3:
# Input:
nums = [5, 4, 9, 11]
print(orArray(nums))
# Output: [5,13,11]
