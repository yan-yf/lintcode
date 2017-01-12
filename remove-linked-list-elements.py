# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/remove-linked-list-elements
@Language: Python
@Datetime: 17-01-12 08:20
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if not head:
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            pre = dummy
            while head:
                if head.val == val:
                    pre.next = head.next
                    head = pre
                pre = head
                head = head.next
            return dummy.next