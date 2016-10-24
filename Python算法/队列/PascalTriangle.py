# coding:utf-8

from collections import deque

# k 代表得到第 k 层的杨辉三角图形的数字 ,
# 也是 (a + b)^k  展开式各元素的系数
def PascalTriangle(k):

    # 初始化队列 , 得到杨辉三角第一行数字
    q = deque([1])

    # 0       1
    # 1     1   1     得到这层元素需要进行 1 次循环
    # 2    1  2  1    得到这层元素需要进行 2 次循环
    # 得到第 k 层元素 , 需要 k 次循环（层数从 0 开始计数）
    # i 代表当前循环是生成第 i 层
    for i in range(k):

        # 0       1
        # 1     1   1     第一层需要出队一个元素
        # 2    1  2  1    第二层需要出队二个元素
        # 第 i 层需要出队 i 个元素 , 用来生成第 i + 1 层
        for _ in range(i):
            # q[0] 代表队头元素
            q.append(q.popleft() + q[0])

        # 队尾追加一个 1
        q.append(1)

    # 将队列转化为列表
    return list(q)

if __name__ == '__main__':
    print PascalTriangle(0)



