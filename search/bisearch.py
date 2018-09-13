# encoding:utf-8

# 二分查找
def bisearch(lst, key):
    low, high = 0, len(lst) - 1
    while low <= hight:  # 范围内还有元素
        mid = low + (high - low) // 2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].key:
            high = mid - 1
        else:
            low = mid + 1
