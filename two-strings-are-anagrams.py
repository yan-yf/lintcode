# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 17-01-13 09:24
'''

'''
写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。
给出 s = "abcd"，t="dcab"，返回 true.
给出 s = "ab", t = "ab", 返回 true.
给出 s = "ab", t = "ac", 返回 false.
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        ''.join(s)
        ''.join(t)
        if s == t:
            return True
        return False