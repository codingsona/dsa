def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                min = j
                arr[i], arr[min] = arr[min], arr[i]

    return arr

result = selectionSort([1,2,3,6,7,8,4,9,10,5])

print(result)
