# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 17-01-14 06:31
'''
'''
对于一个给定的 source 字符串和一个 target 字符串，
你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
如果不存在，则返回 -1。
样例
如果 source = "source" 和 target = "target"，返回 -1。
如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。
'''
class Solution:
    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        elif len(target) == 0:
            return 0
        else:
            ls = list(source)
            for i in xrange(len(source)):
                if ''.join(ls[i:i+len(target)]) == target:
                    return i
            return -1