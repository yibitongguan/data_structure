# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/13 21:53
"""
# 基数排序
def radix_sort(lst, d):
    rlists = [[] for i in range(10)]
    llen = len(lst)
    for m in range(-1, -d-1, -1):
        for j in range(llen):
            rlists[lst[j][m]].append(lst[j])  # 先分配
        j = 0
        for i in range(10):
            tmp = rlists[i]
            for k in range(len(tmp)):
                lst[j] = tmp[k]  # 再收集
                j += 1
            rlists[i].clear()

if __name__ == '__main__':
    lst = [(2, 2, 0), (1, 4, 5), (1, 3, 7), (1, 4, 7)]
    radix_sort(lst, 3)
    print(lst)

