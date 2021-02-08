def bubbleSort(arr):
    swapped = True
    counter = 0
    while swapped == True:
        swapped = False
        rp = len(arr) - 1
        lp = rp - 1
        while lp >= counter:
            if arr[lp] > arr[rp]:
                arr[lp],arr[rp] = arr[rp],arr[lp]
                swapped = True
            rp -= 1
            lp -= 1
        counter += 1
    return arr

print(bubbleSort([1,2,5,9,3,4,8,6,0]))