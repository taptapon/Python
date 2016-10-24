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

def levelOrder(root):
    node = root
    q = deque([node])

    while True:
        node = q.popleft()
        print node

        if not node.left == None:
            q.append(node.left)

        if not node.right == None:
            q.append(node.right)

        if not q:
            break

def copyTree(root):
    node = root

    if node is None:
        return

    lt = copyTree(node.left)
    rt = copyTree(node.right)

    node = TreeNode(node.data, lt, rt)

    return node


if __name__ == '__main__':
    root = copyTree(createTree())
    levelOrder(root)