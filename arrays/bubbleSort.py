def bubbleSort(arr):
    rp = len(arr)-1
    lp = rp-1
    swapped = True
    while swapped == True:
        swapped = False
        for rp in range(rp,0,-1):
            if arr[lp] > arr[rp]:
                arr[lp],arr[rp] = arr[rp],arr[lp]
                swapped = True
                lp -= 1
    return arr



print(bubbleSort([5,9,3,1,2,8,4,7,6]))