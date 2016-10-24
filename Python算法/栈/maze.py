# coding:utf-8

def initMaze():
    # 初始化一个空的 7×7 表格
    maze = [[0] * 7 for i in range(0, 7)]
    # 迷宫障碍的位置
    walls = [(1, 3),(1, 5),
            (2, 1), (2, 5),
            (3, 3), (3, 4),
            (4, 2),
            (5, 4)]

    # 最外层一圈设置成 1
    for i in range(0, 7):
        maze[0][i] = 1
        maze[i][0] = 1
        maze[6][i] = 1
        maze[i][6] = 1
    # 迷宫障碍位置设置成 1
    for i, j in walls:
        maze[i][j] = 1

    return maze

def path(maze, start, end):
    # i, j 代表起点的位置
    i, j = start
    # ei, ej 代表终点的位置
    ei, ej = end

    # 用栈来存储出迷宫的路径
    stack = []
    # “ 人 ” 在起点
    stack.append((i, j))
    # “ 人 ” 在起点 , 将走过的位置置为 1
    maze[i][j] = 1

    # 循环一次 , 相当于 “ 人 ”  走一步
    # 如果栈为空 , 则跳出循环 , 空栈代表迷宫走不通
    while stack:
        i, j = stack[-1]
        # “ 人 ” 此时位置已经在终点 , 跳出循环
        if (i, j) == (ei, ej):
            break

        # 循环四次尝试能否向四个方向走
        # 用 di , dj 这种增量的形式表示 “ 人 ” 走一步的距离
        # 四种情况代表 4 个方向
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            # 如果这个方向是 0 代表能走
            if maze[i+di][j+dj] == 0:
                # “ 人 ” 走到这个位置
                stack.append((i+di, (j+dj)))
                # 这个位置置为 1 , 代表走到过这个位置
                maze[i+di][j+dj] = 1
                break
        # 四个方向都是 1 代表无路可走后退一步
        else:
            stack.pop()

    return stack

if __name__ == '__main__':

     print path(initMaze(), (1, 1), (5, 5))