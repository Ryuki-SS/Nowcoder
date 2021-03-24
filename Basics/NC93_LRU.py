

# line = sys.stdin.readline().strip()
# operators = line[2:-4].split("],[")
# k = int(line[-1])
# a = Solution(k)
# for ope in operators:
#     if ope[0] == '1':
#         a.set(int(ope[2]), int(ope[4]))
#     else:
#         a.get(int(ope[2]))
# print(a.res)


"""
设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
set(key, value)：将记录(key, value)插入该结构
get(key)：返回key对应的value值
[要求]
set和get方法的时间复杂度为O(1)
某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
若opt=1，接下来两个整数x, y，表示set(x, y)
若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
对于每个操作2，输出一个答案
示例1
输入
复制
[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
返回值
复制
[1,-1]
说明
第一次操作后：最常使用的记录为("1", 1)
第二次操作后：最常使用的记录为("2", 2)，("1", 1)变为最不常用的
第三次操作后：最常使用的记录为("3", 2)，("1", 1)还是最不常用的
第四次操作后：最常用的记录为("1", 1)，("2", 2)变为最不常用的
第五次操作后：大小超过了3，所以移除此时最不常使用的记录("2", 2)，加入记录("4", 4)，并且为最常使用的记录，然后("3", 2)变为最不常使用的记录
"""

"""
class Solution:
    def LRU(self , operators , k ):
        # write code here```````
        self.dict = collections.OrderedDict()
        self.capacity = k
        self.res = []
        for l in operators:
            if l[0] == 1:
                self.set(l[1], l[2])
            elif l[0] == 2:
                self.get(l[1])
        return self.res

    def get(self, key):
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
            self.res.append(val)
        else:
            self.res.append(-1)

    def set(self, key, value):
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
        else:
            if self.capacity>0:
                self.capacity -= 1
            else:
                self.dict.popitem(last=False)
            self.dict[key] = value
"""