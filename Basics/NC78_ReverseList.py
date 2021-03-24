# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        rev = pHead
        nxt = pHead.next
        rev.next = None
        while nxt:
            tmp = nxt
            nxt = nxt.next
            tmp.next = rev
            rev = tmp
        return rev


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    s = Solution()
    rev = s.ReverseList(a)
    while rev:
        print(rev.val)
        rev = rev.next