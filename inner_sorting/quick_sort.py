# encoding:utf-8

# 快速排序
def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)
    
def qsort_rec(lst, l, r):
    if l >= r:                  # 分段无记录或只有一个记录
        return
    i = l
    j = r
    pivot = lst[i]              # 初始空位
    while i < j:
        while i < j and lst[j] >= pivot:
            j -= 1              # 用j向左扫描找小于pivot的记录
        if i < j:
            lst[i] = lst[j]     # 小记录移到左边
            i += 1
        while i < j and lst[i] <= pivot:
            i += 1              # 用i向左扫描找大于pivot的记录
        if i < j:
            lst[j] = lst[i]
            j -= 1              # 大记录移到右边
    lst[i] = pivot              # 将pivot存入其最终位置
    qsort_rec(lst, l, i-1)      # 递归处理左半区间
    qsort_rec(lst, i+1, r)      # 递归处理右半区间
    
def quick_sort1(lst):
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin]
        i = begin
        for j in range(begin+1, end+1):
            if lst[j] < pivot:  # 发现一个小元素
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]  # 枢轴元就位
        qsort(lst, begin, i-1)  # 递归处理左半区间
        qsort(lst, i+1, end)    # 递归处理右半区间
    
    qsort(lst, 0, len(lst)-1)

if __name__ == '__main__':
    lst = [1, 6, 5, 44, 7, 5, 81, 2]
    # quick_sort(lst)
    quick_sort1(lst)
    print(lst)

