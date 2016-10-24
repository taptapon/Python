# coding:utf-8

from collections import deque

def divison(R, N):
    # 代表笼子的集合
    res = []
    # 代表编号动物 0~n-1 的动物依次入队
    q = deque(range(N))
    # 代表上一个出队动物的编号
    pre = N

    # 队列不为空 , 代表有动物没有进入笼子 , 继续循环
    while q:
        # 代表当前出队的动物
        cur = q.popleft()
        # 之前出队动物编号大于等于当前出队动物编号 , 队列中的动物（包括当前出队的动物 cur）
        # 都已经尝试进入当前笼子 , 但是没能进入 , 需要创建新笼子
        if pre >= cur:
            res.append([])

        # 当前出队的动物尝试进入当前笼子
        for animal in res[-1]:
            # 如果与当前笼子中的动物冲突 , 重新添加到队列尾
            # break 跳出循环体 , 不走 break 的 else
            if (animal, cur) in R:
                q.append(cur)
                break
        else:
            # 如果没有冲突 , 进入当前笼子
            res[-1].append(cur)

        # 下次循环的时候 , 当前出队的动物变成了上次出队的动物
        # while 每次循环代表当前动物能否进入当前笼子
        pre = cur

    return res


if __name__ == '__main__':
    # 0~8 这九个数字需要被划分
    N = 9
    # 0~8 这九个数字的冲突关系
    R = {(1, 4), (4, 8), (1, 8), (1, 7),
         (4, 1), (8, 4), (8, 1), (7, 1),
         (8, 3), (1, 0), (0, 5), (1, 5),
         (3, 8), (0, 1), (5, 0), (5, 1),
         (3, 4), (5, 6), (6, 2), (6, 2), (6, 4),
         (4, 3), (6, 5), (2, 6), (2, 6), (4, 6)}

    print divison(R, N)
