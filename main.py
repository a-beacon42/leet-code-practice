# %%
"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""


def two_sum(nums: list[int], target: int) -> list[int] | None:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
