#插入排序 时间复杂度为O(n**2)
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        x = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time %s secs."%(func.__name__, t2-t1))
    return wrapper

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]  #手摸到的牌
        j = i - 1  #最后一张牌
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j = j - 1
        li[j+1] = tmp


insert = list(range(100000))
insert_sort(insert)
print(insert)