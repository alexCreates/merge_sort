import random
global ten_thousand_list
ten_thousand_list = []
# create a list of ten thousand random numbers between -10,000 and 10,000
for i in range(10001):
    num = random.randint(-10000,10000)
    ten_thousand_list.append(num)

def merge_sort(arr):
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
