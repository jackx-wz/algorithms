import random
def qsort(arr):
    lt_arr = []
    gt_arr = []
    new_arr = []
    print(arr, "#####")
    if len(arr) == 1:
        return arr
    else:
        index = random.randint(0, len(arr)-1)
        print index, arr[index], "\n"
        for idx, ele in enumerate(arr):
            print idx, ele
            if idx == index:
                continue

            if ele <= arr[index]:
                lt_arr.append(ele)
            if ele > arr[index]:
                gt_arr.append(ele)
            print(lt_arr, '<>', gt_arr)
    if len(lt_arr):lt_arr = qsort(lt_arr)
    if len(gt_arr):gt_arr = qsort(gt_arr)
    if len(lt_arr)>0: new_arr = lt_arr
    new_arr = new_arr + [arr[index]]
    if len(gt_arr)>0: new_arr = new_arr + gt_arr

    return new_arr


arr = [3, 4, 5, 2, 8, 7, 1, 9]
print(qsort(arr))
