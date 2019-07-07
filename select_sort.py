#选择排序 时间复杂度O(n**2)
from testSort import quick_sort

@quick_sort.cal_time
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc],li[i] = li[i], li[min_loc]

so = [8,2,0,9,1,7,4,3]
select_sort(so)
print(so)