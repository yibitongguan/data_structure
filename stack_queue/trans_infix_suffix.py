# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/8/30 22:08
"""
from SStack import SStack

priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}  # 运算符优先级
infix_operators = '+-*/()'  # 运算符
"""
将中缀表达式转换为后缀表达式
"""
def trans_infix_suffix(line):
    st = SStack()
    exp = []

    for x in tokens(line):
        if x not in infix_operators:  # 运算对象直接送出
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():  # 没找到左括号
                raise SyntaxError("Missing '('.")
            st.pop()  # 弹出左括号
        else:  # 处理算术运算符，运算符都看作左结合
            while(not st.is_empty() and
                  priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():  # 送出栈里面剩下的运算符
        if st.top() == '(':   # 多余的左括号
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())

    return exp

"""
生成器函数，逐一生成line中的一个个项。项是浮点数或运算符
不能处理一元运算符，也不能处理带符号的浮点数
"""
def tokens(line):
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:  # 运算符
            yield line[i]
            i += 1
            continue

        j = i + 1

        while(j < llen and not line[j].isspace() and
              line[j] not in infix_operators):
            j += 1
        yield line[i:j]     # 生成运算对象子串
        i = j

if __name__ == '__main__':
    s = '(3 - 5) * (6 + 17 * 4) / 3'
    print(s)
    print(trans_infix_suffix(s))
