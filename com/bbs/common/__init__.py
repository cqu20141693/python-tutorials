' a test module '
__author__ = "cc"

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

解题思路
用字典保存遍历过的数字和下标
寻找target-nums[i]是否在字典中出现过，是则返回两数的下标
否则存入nums[i]及其下标
'''


def twoSum(nums: list[int], target: int) -> list[int]:
    dicts = {}
    for i in range(len(nums)):
        if target - nums[i] in dicts:
            return [dicts[target - nums[i]], i]
        else:
            dicts[nums[i]] = i
