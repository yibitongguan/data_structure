# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/8/30 21:27
"""
from SStack import SStack

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

# 定义一个函数把表示表达式的字符串转化为项
def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

"""
计算后缀表达式计算器
"""
def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))      # 不能转换自动引发异常
            continue

        if st.depth() < 2:   # x必为运算符，栈元素不够时引发异常
            raise SyntaxError("Short of operand(s).")
        a = st.pop()  # 取得第二个运算对象
        b = st.pop()  # 第一个运算对象

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break

        st.push(c)

        if st.depth() == 1:
            return st.pop()
        raise SyntaxError("Extra operand(s).")

def suffix_exp_calculator():
    while True:
        try:
            line = input("Suffix Expression:")
            if line == 'end':
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

if __name__ == '__main__':
    suffix_exp_calculator()
