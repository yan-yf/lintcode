# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 17-01-13 09:28
'''
'''
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
样例
给出 A = "ABCD" B = "ACD"，返回 true

给出 A = "ABCD" B = "AABC"， 返回 false
'''

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        A = list(A)
        B = list(B)
        for i in B:
            if i not in A:
                return False
            else:
                del(A[A.index(i)])
        return True