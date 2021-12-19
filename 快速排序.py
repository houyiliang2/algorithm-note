import random
def QuickSort(li):

    if len(li) < 2:                 #运用递归    基线条件（写在函数前面）   列表中元素少于两个一定是有序的  直接返回列表即可
        return li
    else:
        BaseValue = li[0]               #递归条件
        less = [element for element in li[1 : ] if element <= BaseValue]    #所有小于基础值构成的列表

        more = [element for element in li[1 : ] if element > BaseValue]     #所有大于基值构成的列表

        return QuickSort(less) + [BaseValue] + QuickSort(more)

li = list(range(1000))
random.shuffle(li)
print(QuickSort(li))




