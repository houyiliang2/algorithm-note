
import random
#定义一个函数找出数列中最小的值                python 内置了list.min()函数也可以直接用
def findmin(arr):
    min_val = arr[0]
    min_index = 0
    for i in range(1 , len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
            min_index = i
    return min_val                                              #min_index      对应的pop

def SelecSort(arr):
    arr_new = []             #创一个新的数组 用来存放每个找出来的最大值
    for i in range(1 , len(arr)):
        #min_val = min(arr)         内置函数
        min_val = findmin(arr)
        arr_new.append(min_val)
        arr.remove(min_val)                         # .pop()的参数是index 下标

    return arr_new

arr = [random.randint(0 , 100) for i in range(20)]
print(SelecSort(arr))




