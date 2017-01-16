# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/ugly-number
@Language: Python
@Datetime: 17-01-16 09:12
'''
'''
写一个程序来检测一个整数是不是丑数。

丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。
'''

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        l = [2, 3, 5]
        while 1:
            if num == 1:
                return True
            if num == 0:
                return False
            x2, y2 = divmod(num, 2)
            x3, y3 = divmod(num, 3)
            x5, y5 = divmod(num, 5)
            if y2 == 0:
                num = x2
            elif y3 == 0:
                num = x3
            elif y5 == 0:
                num = x5
            else:
                return False
            if num in l:
                return True

            
            