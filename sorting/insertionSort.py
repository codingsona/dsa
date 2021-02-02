def insertionSort(arr):
    # O(N^2) time | O(1) space
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

ins_ar = [1,2,3,4,5,6,8,9,7,10]
result = insertionSort(ins_ar)
print(result)
