#冒泡排序

def bubbleSort(li):
    for i in range(len(li) - 1):
        flag = False
        for j in range(0, len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                flag = True
        if not flag:
            break




li = [1,8,6,7,2,3,8]
#print(li)
bubbleSort(li)
print(li)

