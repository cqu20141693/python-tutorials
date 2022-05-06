from unittest import TestCase

from com.bbs.common import Solution, ListNode


# 编写一个测试类，从unittest.TestCase继承
# unittest.TestCase提供了很多内置的条件判断断言
class TestSolution(TestCase):
    # 以test开头的方法就是测试方法
    def test_two_sum(self):
        solution = Solution()
        nums = [2, 5, 6, 7, 11]
        ret = solution.twoSum(nums, 9)
        # 断言相等
        self.assertEqual(ret, [0, 3])

    # 单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self) -> None:
        print("init before test")

    def tearDown(self) -> None:
        print("handle after test")

    def setUpClass(cls) -> None:
        print("init before class")

    def tearDownClass(cls) -> None:
        print("handle after class")


class TestSolution(TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(1)
        l2 = ListNode(9)
        l = Solution.addTwoNumbers(l1, l2)
        if l:
            print(l)
