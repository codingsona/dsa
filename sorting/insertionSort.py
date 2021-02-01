def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

ins_ar = [4,3,6,9,1,5,2,8,7,10]
result = insertionSort(ins_ar)
print(result)