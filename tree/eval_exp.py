# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/4 22:55
"""
"""
实现二元表达式求值
"""

# 定义几个表达式构造函数
def make_sum(a, b):
    return ('+', a, b)

def make_prod(a, b):
    return ('*', a, b)

def make_diff(a, b):
    return ('-', a, b)

def make_div(a, b):
    return ('/', a, b)

# 判断是否为基本表达式
def is_basic_exp(a):
    return not isinstance(a, tuple)

# 判断是否为数值
def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))

# 求值函数主体
def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    if op == '-':
        return eval_diff(a, b)
    if op == '*':
        return eval_prod(a, b)
    if op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)

# 具体求值函数
def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    return make_sum(a, b)

def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    return make_diff(a, b)

def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    return make_prod(a, b)

def eval_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    if is_number(a) and is_number(b):
        return a / b
    return make_div(a, b)

if __name__ == '__main__':
    e = make_sum(make_prod(3, 5), make_div(4, 2))
    print(e)
    print(eval_exp(e))
