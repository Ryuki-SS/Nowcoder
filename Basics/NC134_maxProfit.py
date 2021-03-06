class Solution:
    def maxProfit(self , prices ):
        profit = 0
        if not prices:
            return 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    a=Solution()
    print(a.maxProfit([1,2,3,4,5]))

"""
假定你知道某只股票每一天价格的变动。
你最多可以同时持有一只股票。但你可以无限次的交易（买进和卖出均无手续费）。
请设计一个函数，计算你所能获得的最大收益。
示例1
输入
复制
[5,4,3,2,1]
返回值
复制
0
说明
由于每天股票都在跌，因此不进行任何交易最优。最大收益为0。

示例2
输入
复制
[1,2,3,4,5]
返回值
复制
4
说明
第一天买进，最后一天卖出最优。中间的当天买进当天卖出不影响最终结果。最大收益为4。
备注:
总天数不大于200000。保证股票每一天的价格在[1,100]范围内。
"""
