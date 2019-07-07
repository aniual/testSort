#快速排序 递归完成排序
#递归排序重新调用函数然后使用装饰器，否则会重复一直调用装饰器

import random
import sys
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        x = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time %s secs."%(func.__name__, t2-t1))
    return wrapper


def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid-1)
        quick_sort_x(data,mid+1,right)


def partition(data,left,right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[right] <= tmp:
            left += 1
        #data[right] = data[left]
    data[left] = tmp
    return left


@cal_time
def quick_sort(data):
    quick_sort_x(data, 0, len(data)-1)


quick = list(range(100000))
random.shuffle(quick)


quick_sort(quick)
print(quick)