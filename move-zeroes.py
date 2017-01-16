# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/move-zeroes
@Language: Python
@Datetime: 17-01-16 08:44
'''
'''给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
'''

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        nzero = 0
        li = []
        for i in nums:
            if i is 0:
                nzero += 1
            else:
                li.append(i)
        li.extend([0] * nzero)
        for i in xrange(len(nums)):
            nums[i] = li[i]
        