"""***Task***"""
"""
Given an input array and toMove element which is an element of the input array. Our task is to 
rearrange the array by moving the toMove element to the end of the array.. 
 """
#O(n) Time | O(1) Space
def moveArray(array,toMove):
    l=0
    r=len(array)-1
    while l < r:
        while array[r] == toMove:
            if r == l:
                return array
            r -= 1
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
        l += 1
    return array

array = [2,1,2,2,3,4,2]
toMove = 2
print(moveArray(array,toMove))