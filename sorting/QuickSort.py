def quickSort(array):
    # O(NlogN) time | O(logN) space
    recursiveQs(array, 0, len(array)-1)
    return array

def recursiveQs(arr, start, end):
    # base case
    if start >= end:
        return

    pivot = end
    lp = start
    rp = end-1

    #print(lp, rp, pivot, arr)

    while lp <= rp:
        if arr[lp] > arr[pivot] and arr[rp] < arr[pivot]:
            arr[lp], arr[rp] = arr[rp], arr[lp]

        if arr[lp] < arr[pivot]:
            lp += 1

        if arr[rp] >= arr[pivot]:
            rp -= 1

        #print(lp, rp, arr)

    arr[lp], arr[pivot] = arr[pivot], arr[lp]

    if start - lp + 1 < end - lp - 1:
        recursiveQs(arr, start, lp-1)
        recursiveQs(arr, lp + 1, end)
    else:
        recursiveQs(arr, lp + 1, end)
        recursiveQs(arr, start, lp - 1)


print(quickSort([4, 12, 6, 8, 9, 7, 1, 3, 9, 2, 5]))

print(quickSort([4, 3, 1, 6]))


