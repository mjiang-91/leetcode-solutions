# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None:
            return None
        else:
            l1_next = None
            l2_next = None
            summary = 0
            carry = 0
            
            if l1 is not None:
                summary += l1.val
                l1_next = l1.next
            
            if l2 is not None:
                summary += l2.val
                l2_next = l2.next
            
            carry = summary // 10
            mod = summary % 10
            result = ListNode(mod)

            if carry != 0:
                if l1_next is not None:
                    l1_next.val += carry
                    result.next = self.addTwoNumbers(l1_next, l2_next)
                elif l2_next is not None:
                    l2_next.val += carry
                    result.next = self.addTwoNumbers(l1_next, l2_next)
                elif l1_next is None and l2_next is None:
                    result.next = ListNode(carry)
            else:
                    result.next = self.addTwoNumbers(l1_next, l2_next)                
            return result


def test_solution():
    # TODO
    pass
