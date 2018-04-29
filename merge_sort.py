
import random
global ten_thousand_list
ten_thousand_list = []
# create a list of ten thousand random numbers between -10,000 and
for i in range(10001):
    num = random.randint(-10000,10000)
    ten_thousand_list.append(num)



def merge_sort(arr):
    """Inplace merge sort of array without recursive. The basic idea
    is to avoid the recursive call while using iterative solution.
    The algorithm first merge chunk of length of 2, then merge chunks
    of length 4, then 8, 16, .... , until 2^k where 2^k is large than
    the length of the array
    """

    num = 1
    while num <= len(arr):
        x = 0
        for x in range(0, len(arr), num * 2):
            left, right = x, min(len(arr), x + 2 * num)
            mid = x + num
            # merge arr[x:x + 2 * num]
            l = left
            m = mid
            while left < mid and mid < right:
                if arr[l] < arr[m]: l += 1
                else:
                    tmp = arr[m]
                    arr[l + 1: m + 1] = arr[l:m]
                    arr[l] = tmp
                    l, mid, m = l + 1, mid + 1, m + 1
        num *= 2
    print arr

merge_sort(ten_thousand_list)













### failing merge sort not sorting!! ###

# def merge_sort(arr):
#     print 'moving to merge_laler2'
#     print '-' * 50
#     merge_layer2(arr, 0, len(arr)-1)
#
# def merge_layer2(arr, first, last):
#     # first = 0 last = 11
# 	if first < last:
# 		middle = (first + last)//2
# 		merge_layer2(arr, first, middle)
# 		merge_layer2(arr, middle+1, last)
# 		merge(arr, first, middle, last)
#
# def merge(arr, first, middle, last):
# 	L = arr[first:middle+1]
# 	R = arr[middle+1:last+1]
# 	L.append(sys.maxsize)
# 	R.append(sys.maxsize)
# 	i = j = 0
#
# 	for k in range (first, last+1):
# 		if L[i] <= R[j]:
# 			arr[k] = L[i]
# 			i += 1
# 		else:
# 			arr[k] = R[j]
# 			j += 1
#
# arr = [ten_thousand_list]
# print 'before = ' + str((arr))
# merge_sort(arr)
# print 'after = ' + str((arr))
