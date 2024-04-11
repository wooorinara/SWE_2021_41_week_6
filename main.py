from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
# YOUR ANSWER
    n = len(nums)
    for i in range(n):
        for j in range(i +1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

nums_input = input("Input: ")
nums = [int(num) for num in nums_input.split(",")]
target = int(input("Target2: "))
print(twoSum(nums, target))
