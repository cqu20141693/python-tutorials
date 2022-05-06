"""
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
import 模块名 as 别名
"""
from typing import Optional

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        # 定义dict
        dicts = {}
        # 循环list
        for i in range(len(nums)):
            if target - nums[i] in dicts:
                # 如果目标-当前数字结果在dict中，返回结果
                return [dicts[target - nums[i]], i]
            else:
                # 缓存遍历过的数字
                dicts[nums[i]] = i

    """
    Optional ： 可以用于判断变量是否存在
    
    and or not : 与或非
    
    is not /is 比较 id是否相同
    == 用于比较值是否相等
    """

    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字

        :param l1:  第一个数
        :param l2: 第二个数
        :return:
        """
        if l1:
            if l2:

                head = None
                curr = head
                carry = 0
                while l1 is not None or l2 is not None or carry != 0:
                    node = ListNode()
                    val_carry = 0

                    if l2 is None:
                        if l1 is None:
                            val_carry = carry
                            carry = 0
                        else:
                            val_carry = l1.val + carry
                    elif l1 is None:
                        val_carry = l2.val + carry
                    else:
                        val_carry = l1.val + l2.val + carry

                    if val_carry > 9:
                        node.val = val_carry - 10
                        carry = 1
                    else:
                        node.val = val_carry
                        carry = 0
                    if head is None:
                        head = node
                        curr = node
                    else:
                        curr.next = node
                        curr = node
                    if l1 is not None:
                        l1 = l1.next
                    if l2 is not None:
                        l2 = l2.next
                return head
            else:
                return l1
        else:
            if l2:
                return l2
            else:
                return None
