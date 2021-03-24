class Solution:
    def jumpFloor(self, number):
        # if number <= 1:
        #     return 1
        # else:
        #     return self.jumpFloor(number-1)+self.jumpFloor(number-2)
        a, b = 0, 1
        for _ in range(number + 1):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    x = Solution()
    print(x.jumpFloor(35))

"""
14930352
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""