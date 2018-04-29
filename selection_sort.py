# creating a list of ten thousand random numbers between -10,000 and +10,000 for run time
# avg run time 8.901s <--- o_0
import random
global ten_thousand_list
ten_thousand_list = []
for i in range(10001):
    num = random.randint(-10000,10000)
    ten_thousand_list.append(num)



def selection_sort(arr):
    for i in range(len(arr)):
        low = i
        x = i + 1
        while(x < len(arr)):
            if(arr[x] < arr[low]):
                low = x
            x += 1
        arr[i], arr[low] = arr[low], arr[i]
    print arr

selection_sort(ten_thousand_list)
