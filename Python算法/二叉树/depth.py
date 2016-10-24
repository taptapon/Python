# coding:utf-8

from collections import deque

class TreeNode(object):

    # data 节点的数据
    # left 左节点 right 右节点
    # left = None right = None 默认生成的是叶节点
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 重写 str 方法
    # print TreeNode 对象的时候 , 打印出相应的 data
    def __str__(self):
        return str(self.data)

def createTree():
    # 通过列表拆包的形式创建多个节点（此时节点都没有左节点与右节点 , 都是孤立的）
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']

    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I

    return A

def depth(node):

    if node is None:
        return 0

    dl = depth(node.left)
    dr = depth(node.right)

    return max(dl, dr) + 1

def depth2(root):
    q = deque([(root, 1)])

    while True:
        node, d = q.popleft()

        if node.left:
            q.append((node.left, d+1))
        if node.right:
            q.append((node.right, d+1))

        if not q:
            break

    return d

if __name__ == '__main__':
    print depth2(createTree())