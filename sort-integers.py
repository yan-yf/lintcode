# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/sort-integers
@Language: Python
@Datetime: 17-01-12 06:57
'''

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in xrange(len(A) - 1):
            for j in xrange(len(A) - i - 1):
                if A[j] >= A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]