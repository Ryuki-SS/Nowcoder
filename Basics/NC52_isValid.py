#
#
# @param s string字符串
# @return bool布尔型
#

class Solution:
    def isValid(self, s):
        # write code here
        stk = []
        for c in s:
            if c == ')':
                if stk == [] or stk.pop() != '(':
                    return False
            elif c == '}':
                if stk == [] or stk.pop() != '{':
                    return False
            elif c == ']':
                if stk == [] or stk.pop() != '[':
                    return False
            else:
                stk.append(c)
        return False if stk else True

"""
class Solution:
    def isValid(self , s ):
        # write code here
        #长度为奇数 一定不对
        if len(s)%2 == 1:
            return False
        #只有3种括号在s中，才进行替换
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('[]','').replace('{}','').replace('()','')
        return True if s=='' else False
"""

