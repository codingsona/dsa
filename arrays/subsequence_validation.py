"""***Task***"""
"""Here we will do validation that a sub sequence will be there in an array.If all the elements
 of the subsequence array are there in the array, it will return True else it ll return False."""

def validate(array, subsequence):
    counter = 0
    for elem in array:
        if elem == subsequence[counter]:
            counter += 1
            if counter == len(subsequence):
                return True

    return False

    """if counter == len(subsequence):
        return True
    else:
        return False"""

arr = [5,1,22,25,6,-1,8,10]
subseq = [1,6,-1,10]
print(validate(arr, subseq))