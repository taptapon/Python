# coding:utf-8

def match(expr):

    # 定义左括号
    LEFT = {'{', '(', '['}
    # 定义右括号
    RIGH = {'}', ')', ']'}

    expr = filter(lambda char: True if char in LEFT | RIGH else False, expr)

    # 空列表用来存储待消除左括号
    stack = []

    for char in expr:
        # 如果是左括号 , 进栈
        if char in LEFT:
            stack.append(char)
        # 如果是右括号
        elif char in RIGH:
            # 如果此时已经是空栈 , 说明右括号多了 , 匹配出错
            if not stack:
                return u'匹配出错 ，右括号多'
            # 如果此时栈顶元素与右括号 , 匹配不上 , 匹配报错
            elif not 0 < ord(char) - ord(stack[-1]) <= 2:
                return u'匹配出错 ，匹配不上'
            # 匹配成功 , 栈顶元素出栈
            stack.pop()

    if not stack:
        return u'匹配成功'
    # 匹配结束 , 非空栈 , 说明左括号多了 , 匹配出错
    else:
        return u'匹配出错 ，左括号多'


if __name__ == '__main__':

    expr = '{{d(a[]a)}+}'

    print match(expr)




