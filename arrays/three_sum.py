def three_num_sum(array, targetSum):
    result = []
    array.sort()
    print(array)

    for i in range(len(array) - 1):
        l = i+1
        r = len(array) - 1
        threeSum = array[i] + array[l] + array[r]
        #print(i, l, r, threeSum)

        while l < r:
            threeSum = array[i] + array[l] + array[r]
            print(i, l, r, threeSum)
            if threeSum < targetSum:
                l = l+1
            elif threeSum > targetSum:
                r = r - 1
            else:
                result.append((i, l , r))


        #'''
    return result

array = [12,3,1,2,-3,4,5,6,7]
targetSum = 0
print(three_num_sum(array,targetSum))