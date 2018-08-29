# encoding:utf-8

# 朴素串匹配算法
def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:             # 字符相同，考虑下一对字符
            i, j = i + 1, j + 1
        else:                        # 字符不同，考虑目标串t中下一位置
            i, j = 0, j - i + 1
    if i == m:                       # 找到匹配，返回其开始下标
        return j - i
    return -1                        # 无匹配，返回特殊值
    
# KMP串匹配，主函数
def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:   # 考虑p中下一字符
            j, i = j + 1, i + 1
        else:                         # 失败，考虑pnext决定的下一字符
            i = pnext[i]
    if i == m:
        return j - i
    return -1

"""
生成针对p中各位置i的下一检查位置表，用于KMP算法
优化版本
"""
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:    # 生成下一个pnext元素
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext
    
if __name__ == '__main__':
    print(gen_pnext('abbcabcaabbcaa'))
            
