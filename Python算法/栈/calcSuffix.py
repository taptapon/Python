# coding:utf-8

def calcSuffix(str):

    # 定义操作符
    operator = {
        '+':lambda op1, op2: op1+op2,
        '-':lambda op1, op2: op1-op2,
        '*':lambda op1, op2: op1*op2,
        '/':lambda op1, op2: op1/op2
    }

    # 栈用来存储
    stack = []

    # 后缀表达式是用字符串的形式给出的 , 操作数、操作符通过空格分隔
    # 通过 split() 方法将数字、操作符分隔成一列表方便后续迭代操作
    parts = str.split()

    for part in parts:
        # 如果是数字（字符形式） , 压栈
        # int() 函数 , 强制转换成数字
        if part.isdigit():
            stack.append(int(part))
        # 如果是操作符 , 弹出栈顶两个元素 , 用于计算
        # 计算结果继续压入栈中
        elif part in operator:
            operation = operator[part]
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(operation(op1, op2))

    # 最后栈中只有一个元素 , 就是后缀表达式计算结果
    return stack[-1]

if __name__ == '__main__':

    print calcSuffix('2 3 4 * +')