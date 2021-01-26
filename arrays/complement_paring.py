"""***Task***"""
"""
We are given with an input list containing all integers and a target sum. we have to create 
ditinct pairs and store them in another list.e.g- input be like [4,5,8,7,6,10,2,3] ,
target=12 and expected output is a list like this [(4,8),(5,7),(10,2)]
"""

def complementing_number_pair(in_list,target_sum):
    # O(N) time | O(N) space
    result_list = []
    hashT = {}
    for elem in in_list:
        expN = target_sum - elem
        if expN in hashT:
            result_list.append((elem, expN))
        else:
            hashT[elem] = expN
    return result_list




l = [4,5,8,7,6,10,2,-8]
target = 0

print(complementing_number_pair(l,target))
