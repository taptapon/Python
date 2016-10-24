# coding:utf-8

from collections import deque

def a_to_b(a, b):
    # 用元组这种数据结构表示 (计算结果, 层数)
    # 通过层数得知通过几次计算由 a 得到 b
    q = deque()
    cur = (a, 0)

    # 如果计算结果不等于 b , 再次计算 计算结果的+1、-1、*2 入队
    while not cur[0] == b:
        # 使用各自的变量存储计算次数
        q.append((cur[0] + 1, cur[1] + 1))
        q.append((cur[0] - 1, cur[1] + 1))
        q.append((cur[0] * 2, cur[1] + 1))
        cur = q.popleft()
    return cur[1]

if __name__ == "__main__":
    print u'通过', a_to_b(3, 11), u'次计算实现！'
