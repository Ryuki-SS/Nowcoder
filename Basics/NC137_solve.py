class Solution:
    def solve(self, s):
        # write code here
        return eval(s)


if __name__ == "__main__":
    str = "(2*(3-4))*5"
    a = Solution()
    print(a.solve(str))
