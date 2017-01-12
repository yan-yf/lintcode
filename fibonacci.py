# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/fibonacci
@Language: Python
@Datetime: 17-01-12 07:44
'''

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a = 0
            b = 1
            r = 0
            for i in range(2, n):
                r = a + b
                a, b = b, r
            return r