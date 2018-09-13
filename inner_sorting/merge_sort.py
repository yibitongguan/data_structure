# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/13 21:20
"""

# 处理两个分段中都有未归并元素
def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:  # 反复复制两分段首记录中较小的
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:  # 复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:  # 复制第二段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1

# 实现一遍归并
def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen <llen:  # 归并长度为slen的两段
        merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2 * slen
    if i + slen < llen:  # 剩下两段，第二段长度小于slen
        merge(lfrom, lto, i, i+slen, llen)
    else:  # 只剩下最后一段,复制到表lto
        for j in range(i, llen):
            lto[j] = lfrom[j]

# 主函数
def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)  # 保证结果最后存回原位
        slen *= 2

if __name__ == '__main__':
    lst = [1, 6, 5, 44, 7, 5, 81, 2]
    merge_sort(lst)
    print(lst)
