def binary_search(list , item):          #传入有序数列 ， 要查找的数
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        if list[mid] == item:
            return mid
        if list[mid] > item:         #要找的数item 在guess数的左边
            high = mid - 1
        else:
            low = mid + 1
    return -1                               #表示没找到

list1 = list(range(100))
print(binary_search(list1, 45))

