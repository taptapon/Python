# coding:utf-8

# t 背包剩余空间
# w 物品列表
def knapSack(t, w):

    # 背包 , 存放物品的在列表中的位置
    stack = []
    # 游标 , 指向将要可能入栈元素（有可能入栈元素的位置）
    # 所谓有可能就是加上这个元素背包重量不超过 10 KG
    k = 0
    # 物品数量
    n = len(w)

    # 代表的是什么？回溯法的循环
    # 回溯法最后都到了判断栈是否为空
    while stack or k < n:
        # 代表的是什么？代表一次装备包的过程
        # t > 0 说明背包中还有空间
        # k < n 说明还有物品没有尝试放进背包（进栈）
        # 满足这两个条件时 , 物品才能装入背包
        while t > 0 and k < n:
            if t >= w[k]:
                stack.append(k)
                t = t - w[k]
            # 指向下一个可能装入背包的物品
            k = k + 1

        # 如果这个装备包的过程使得背包中空间为 0
        # 打印结果
        if t == 0:
            print stack

        # 回溯法 , 尝试其他结果
        k = stack.pop()
        t = t + w[k]
        k = k + 1

if __name__ == '__main__':
    w = [1, 8 ,4, 5]
    t = 10

    knapSack(t, w)
